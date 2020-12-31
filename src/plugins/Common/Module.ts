import {ModuleOption} from "./ModuleOption";
import {ModuleMethod} from "./ModuleMethod";
import {ToSnakeCase} from "../../utils/helper";
import {ModuleExample} from "./ModuleExample";

export class Module {

    constructor(swaggerModule: any, isInfoModule:boolean) {
        this.IsInfoModule = isInfoModule;
        this.Init(swaggerModule);
    }
    private Init(swaggerModule: any){
        this.SwaggerName = swaggerModule["$key"];
        this.GetObjectName(swaggerModule["$key"]);
        this.ObjectNamePythonized = ToSnakeCase(this.ObjectName);
        this.GetModuleClassName();
        this.GetModuleName();
        this.ModuleOperationName = ToSnakeCase(swaggerModule["$key"]);
        this.LoadMethods(swaggerModule.operations);
        if (!this.IsInfoModule)
            this.GetBaseCRUDUrl();
        this.GetSpecOptions();
        this.GetResponseFields();
        this.ModuleApiVersion = swaggerModule.operations[0].apiVersions[0].version;
    }

    private LoadExamples(method: ModuleMethod, extensions:any){
        if (method.Name == "get" && !this.IsInfoModule)
            return;
        if (extensions != null && extensions['x-ms-examples'] != null){
            let examples = extensions['x-ms-examples'];
            for (let name in examples){
                if (!this.HasExample(name)){
                    let moduleExample = new ModuleExample(name, examples[name] ,method);
                    this.ModuleExamples.push(moduleExample);
                }
            }
        }

    }

    private HasExample(name: string){
        for (let example of this.ModuleExamples)
            if (example.Name == name)
                return true;
        return false;
    }

    private GetResponseFields(){
        for (let method of this.ModuleMethods){
            for (let option of method.ResponseOptions){
                let moduleOption = this.GetResponseOption(option.Name);
                if (moduleOption != null){
                    if (moduleOption.Documentation.indexOf(option.Documentation) == -1)
                        moduleOption.Documentation = moduleOption.Documentation + "\n" + option.Documentation;
                }
                else
                    this.ModuleResponseFields.push(option);
            }
        }
    }

    private GetResponseOption(name:string){
        for (let option of this.ModuleResponseFields){
            if (option.Name == name)
                return option;
        }
        return null;
    }

    private GetSpecOptions(){
        for (let method of this.ModuleMethods){
            for (let option of method.Options){
                let moduleOption = this.GetModuleOption(option.Name);
                if (moduleOption != null){
                    if (moduleOption.Documentation.indexOf(option.Documentation) == -1)
                        moduleOption.Documentation = moduleOption.Documentation + "\n" + option.Documentation;
                }
                else
                    this.ModuleOptions.push(option);
            }
        }

        for (let modelOption of this.ModuleOptions){
            modelOption.Required = true;
            for (let method of this.ModuleMethods){
                let contains = false;
                for (let methodOption of method.Options){
                    if (methodOption.Name == modelOption.Name){
                        contains = true;
                        break
                    }

                }
                if (!contains) {
                    modelOption.Required = false;
                    break;
                }
            }
        }
    }
    private GetBaseCRUDUrl(){
        for (let method of this.ModuleMethods){
            let httpMethod = method.HttpMethod;
            if (httpMethod == 'put' || httpMethod == 'patch' || httpMethod == 'delete'){
                this.BasicURL = method.Url;
                return;
            }
        }
    }
    private LoadMethods(swaggerMethods:any){
        for (let swaggerMethod of swaggerMethods){
            let moduleMethod = new ModuleMethod(this.ObjectName, swaggerMethod);
            if (this.IsInfoModule && moduleMethod.HttpMethod != 'get' )
                continue;

            if (!this.IsInfoModule && moduleMethod.Name != 'create_or_update' && moduleMethod.Name != 'create'
                && moduleMethod.Name != 'update' && moduleMethod.Name != 'delete' && moduleMethod.Name != 'get' )
                continue;
            this.ModuleMethods.push(moduleMethod);
            this.LoadExamples(moduleMethod, swaggerMethod.extensions);
        }
    }
    private GetModuleClassName(){
        if (this.IsInfoModule)
            this.ModuleClassName =  "AzureRM" + this.ObjectName +"Info";
        else
            this.ModuleClassName =  "AzureRM" + this.ObjectName;
    }

    private GetModuleName(){
        if (this.IsInfoModule)
            this.ModuleName =  "azure_rm_"+this.ObjectName.toLowerCase()+"_info";
        else
            this.ModuleName =  "azure_rm_"+this.ObjectName.toLowerCase();
    }
    private GetObjectName(swaggerName: any)
    {
        // XXX - handle following rules
        // Nat --> NAT
        // I P --> IP
        // Sql --> SQL

        let name: string = swaggerName;

        if (name.endsWith("ies"))
        {
            name = name.substring(0, name.length - 3) + "y";
        }
        else if (name.toLowerCase().endsWith("xes"))
        {
            name = name.substring(0, name.length - 2);
        }
        else if (name.endsWith('s'))
        {
            name = name.substring(0, name.length - 1);
        }
        this.ObjectName = name;
    }
    private GetModuleOption(name: string):ModuleOption{
        for (let option of this.ModuleOptions){
            if (option.Name == name)
                return option;
        }
        return null;
    }
    public SwaggerName: string = null;
    public ModuleName: string = null;
    public PythonNamespace: string = null;
    public PythonMgmtClient: string = null;
    public ModuleClassName: string = null;
    public ModuleOptions: ModuleOption[] = [];
    public ModuleApiVersion: string = null;
    public MgmtClientName: string = null;
    public ModuleMethods: ModuleMethod[] = [];
    public ObjectName: string = null;
    public BasicURL: string = null;
    public LocationDisposition: string = null;
    public DeleteResponseNoLogFields: string[] = [];

    public NeedsDeleteBeforeUpdate: boolean = false;
    public NeedsForceUpdate: boolean;
    public ModuleOperationName: string = null;
    public ObjectNamePythonized: string = null;
    public ModuleResponseFields: ModuleOption[] = [];
    public IsInfoModule: boolean = false;
    public ModuleExamples: ModuleExample[] = [];
    public GetMethod(methodName:string): ModuleMethod{
        for (let method of this.ModuleMethods){
            if (method.Name == methodName)
                return method;
        }
        return null;
    }

    public SupportsTags():boolean{
        return false;
    }

    public GetMethodOptions(methodName:string, bo:boolean):ModuleOption[]{
        for (let method of this.ModuleMethods){
            if (methodName == method.Name)
                return method.Options;
        }
        return null;
    }

    public HasCreateOrUpdate(): boolean{
        for (let method of this.ModuleMethods){
            if (method.Name == "create_or_update")
                return true;
        }
        return false;
    }

    public HasResourceGroup(): boolean{
        return false;
    }
}
