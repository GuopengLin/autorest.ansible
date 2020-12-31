import {Dictionary} from "@azure-tools/linq";
import { SwaggerModelType, ToSnakeCase} from "../../utils/helper";

export enum ModuleOptionKind{
    MODULE_OPTION_PATH,
    MODULE_OPTION_BODY,
    MODULE_OPTION_PLACEHOLDER,
    MODULE_OPTION_HEADER,
    MODULE_OPTION_QUERY,
    MODULE_OPTION_RESPONSE
}


export class ModuleOption {

    constructor(objectName: string, swaggerOption:any, parent: ModuleOption, isResponse : boolean, optionSet: Set<string>) {
        this.padding = "    ";
        if (parent != null)
            this.padding = this.padding + parent.padding;
        this.Parent = parent;
        this.IsResponse = isResponse;
        this.OptionSet = optionSet;
        this.ModuleObjectName = objectName;
        this.Init(swaggerOption);
        // set optionset point to null to avoid the heap space overflow
        this.OptionSet = null;
    }
    private Init(swaggerOption:any){
        this.Name = swaggerOption.language.default.name;
        this.NameAnsible = ToSnakeCase(this.Name);
        if (this.NameAnsible == "resource_group_name")
            this.NameAnsible = "resource_group";
        if (this.NameAnsible == ToSnakeCase(this.ModuleObjectName)+"_name")
            this.NameAnsible = "name";
        this.NameSwagger = this.Name;
        this.Required = swaggerOption.required != undefined ? swaggerOption.required : false;
        this.Documentation = swaggerOption.language.default.description;
        this.IncludeInDocumentation = true;
        this.IncludeInArgSpec = true;
        this.ReadOnly = swaggerOption.readOnly == undefined ? false: swaggerOption.readOnly;
        // This needs to be changed, I don't find a field which determines updatable
        this.Updatable = !this.ReadOnly;
        this.LoadSchema(swaggerOption.schema);
        this.LoadProtocal(swaggerOption.protocol);
    }

    private LoadSchema(schema:any){
        this.Type = this.ParseType(schema.type);
        this.SwaggerType = schema.type;
        //avoid infinite recursion
        if (this.OptionSet.has(this.Name))
            return;
        //add this option name and delete it before return
        this.OptionSet.add(this.Name);
        if (schema.properties != undefined){
            let readOnly = true;
            for (let subParameter of schema.properties){
                let subOption = new ModuleOption(this.ModuleObjectName, subParameter,this, this.IsResponse, this.OptionSet);
                if (!subOption.ReadOnly)
                    readOnly = false;
                if (!subOption.ReadOnly)
                    this.SubOptions.push(subOption);
            }
            this.ReadOnly = readOnly;
        }

        if (schema.type == SwaggerModelType.SWAGGER_MODEL_ARRAY){
            let readOnly = true;
            this.ElementType = this.ParseType(schema.elementType.type);
            if (schema.elementType.type == SwaggerModelType.SWAGGER_MODEL_OBJECT){
                for (let subParameter of schema.elementType.properties){
                    let subOption = new ModuleOption(this.ModuleObjectName, subParameter,this, this.IsResponse, this.OptionSet);
                    if (!subOption.ReadOnly)
                        readOnly = false;
                    if (!subOption.ReadOnly)
                        this.SubOptions.push(subOption);
                }
            }else {
                readOnly = false;
            }
            this.ReadOnly = readOnly;
        }

        if (schema.type == SwaggerModelType.SWAGGER_MODEL_ENUM){
            for (let choice of schema.choices){
                this.EnumValues.push(choice.value);
            }
        }
        // delete this option name before return
        this.OptionSet.delete(this.Name);
    }

    private LoadProtocal(protocol:any){
        if (protocol == undefined)
            return;
        if ( protocol.http != undefined && protocol.http.in != undefined) {
            let location = protocol.http.in;
            if (location == "url") {
                this.Kind = ModuleOptionKind.MODULE_OPTION_PATH;
            } else if (location == "path") {
                this.Kind = ModuleOptionKind.MODULE_OPTION_PATH;
                this.IncludeInArgSpec = true;
            } else if (location == "body") {
                this.Kind = ModuleOptionKind.MODULE_OPTION_BODY;
                this.GetDisposition();
                this.IncludeInArgSpec = true;
            } else if (location == "header") {
                this.Kind = ModuleOptionKind.MODULE_OPTION_HEADER;
            } else if (location === "query") {
                this.Kind = ModuleOptionKind.MODULE_OPTION_QUERY;
            } else {
                this.Kind = ModuleOptionKind.MODULE_OPTION_PATH;
                this.IncludeInArgSpec = true;
            }
        } else {
            this.Kind = ModuleOptionKind.MODULE_OPTION_BODY;
            this.GetDisposition();
            this.IncludeInArgSpec = true;
        }
    }

    private GetDisposition(){
        if (this.Parent == null || this.Parent == undefined){
            if (this.NameSwagger == 'location' || this.NameSwagger =='tags' ||
                this.NameSwagger == 'identity' ||  this.NameSwagger == 'sku'){
                this.DispositionRest =  "/"+this.NameSwagger;
            }
            else
                this.DispositionRest =  "/properties/"+this.NameSwagger;
            this.DispositionSdk = "/"+ToSnakeCase(this.NameSwagger);
        }else {
            this.DispositionSdk = ToSnakeCase(this.NameSwagger);
            this.DispositionRest =   this.NameSwagger;
        }
    }

    private ParseType(type: string) {
        if (type == SwaggerModelType.SWAGGER_MODEL_STRING)
            return 'str';
        if (type == SwaggerModelType.SWAGGER_MODEL_ARRAY)
            return 'list';
        if (type == SwaggerModelType.SWAGGER_MODEL_BOOLEAN)
            return 'bool';
        if (type == SwaggerModelType.SWAGGER_MODEL_DATETIEM )
            return 'str';
        if (type == SwaggerModelType.SWAGGER_MODEL_INTEGER_32 || type == SwaggerModelType.SWAGGER_MODEL_INTEGER_64 || type == SwaggerModelType.SWAGGER_MODEL_INTEGER)
            return 'int';
        if (type == SwaggerModelType.SWAGGER_MODEL_OBJECT || type == SwaggerModelType.SWAGGER_MODEL_DICTIONARY)
            return 'dict';
        if (type == SwaggerModelType.SWAGGER_MODEL_ENUM)
            return 'str';
        if (type == SwaggerModelType.SWAGGER_MODEL_DURATION)
            return 'str';
        return type;
    }

    public NameSwagger: string = null;
    public Name: string = null;

    //Model type name.
    public NameInModelSchema: string = null;

    public IdPortion: string = null;
    public Type: string = null;
    public ItemType: string = null;
    public SwaggerType: string = null;
    //indicate if the option is an arry
    public IsList: boolean = false;
    //indicate if the option is a map
    public IsMap: boolean = false;

    public Required: boolean = false;
    public ReadOnly: boolean = false;
    public Documentation: string = null;
    public DefaultValue: string = null;
    public IncludeInDocumentation: boolean = false;
    public IncludeInArgSpec: boolean = false;
    public NoLog: boolean = false;
    public SubOptions: ModuleOption[] = [];
    public NameAnsible: string = null;
    public ExampleValue: string = null;
    public Hidden: boolean;
    public DispositionSdk: string = null;
    public EnumValues: string[] = [];
    public Comparison: string = null;
    public Updatable: boolean = true;
    public DispositionRest: string = null;
    public NamePythonSdk: string = null;
    public Kind:ModuleOptionKind;
    public SwaggerPath: string[]= [];
    public Computed: boolean;
    public ElementType: string = null;
    public SwaggerOption: any;
    public Parent: ModuleOption;
    public IsResponse: boolean;
    public OptionSet: Set<string>;
    public padding: string;
    public ModuleObjectName: string;
}
