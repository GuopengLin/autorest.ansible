
import { SwaggerModelType, ToSnakeCase, TrimPackageName, Uncapitalize} from "../../utils/helper";
import {pascalCase} from "@azure-tools/codegen";
import {CodeModel, Info} from "@azure-tools/codemodel";
import {Module} from "./Module";
import {ModuleMethod} from "./ModuleMethod";
import {ModuleOption, ModuleOptionKind} from "./ModuleOption";
import {Session} from "@azure-tools/autorest-extension-base";
import {Test} from "./Test";

export class AnsibleCodeModel {
    private model: any = null;
    public Modules: Module[] = [];
    public Tests: Test[] = [];
    private log: Function;
    constructor(model: any, chooseModule: string, onlyList:boolean, log: Function) {
        this.model = model;
        this.log = log;
        if (onlyList)
            this.ListModule();
        else
            this.Init(chooseModule);
    }
    private ListModule(){
        for (let module of this.model.operationGroups) {
            this.log(module["$key"]);
        }
    }
    private Init(chooseModule: string){
        for (let module of this.model.operationGroups){
            if (chooseModule != null && module["$key"] != chooseModule )
                continue;
            let mainModule = new Module(module, false);
            let infoModule = new Module(module, true);

            mainModule.MgmtClientName ="GenericRestClient";
            mainModule.PythonMgmtClient = this.model.info.pascal_case_title;

            let idx = this.model.info.title.indexOf("ManagementClient") != -1? this.model.info.title.indexOf("ManagementClient") :this.model.info.title.indexOf("Client");

            mainModule.PythonNamespace = "azure.mgmt."+ this.model.info.title.substring(0,idx).toLowerCase();
            infoModule.MgmtClientName = "GenericRestClient";
            infoModule.PythonMgmtClient =  this.model.info.pascal_case_title;
            infoModule.PythonNamespace = "azure.mgmt."+ this.model.info.title.substring(0,idx).toLowerCase();
            this.Modules.push(mainModule);
            this.Modules.push(infoModule);

            let test = new Test(mainModule.ModuleName, mainModule.ModuleMethods, mainModule.ObjectName);
            this.Tests.push(test);

            // let mainModule = new Module(module["$key"], false);
            // mainModule.BasicURL = this.GetBasicCRUDUrl(module.operations);
            // mainModule.ModuleApiVersion = module.operations[0].apiVersions[0].version;

            // mainModule.PythonNamespace = "azure.mgmt."+ this.model.info.python_title.split("_")[0];
            // let infoModule = new Module(module["$key"], true);
            // infoModule.BasicURL = this.GetBasicCRUDUrl(module.operations);
            // infoModule.PythonNamespace = "azure.mgmt."+ this.model.info.python_title.split("_")[0];
            // infoModule.ModuleApiVersion = module.operations[0].apiVersions[0].version;
            // infoModule.PythonMgmtClient = this.model.info.title;
            // for (let method of module.operations){
            //     if( method.requests[0].protocol.http.method == "get"){
            //         this.AddMethod(method, infoModule);
            //     }
            //     this.AddMethod(method, mainModule);
            // }
            // this.AddModelModuleoptions(infoModule);
            // this.AddModelModuleoptions(mainModule);

        }
    }
    // private AddModelModuleoptions(module:Module){
    //     for (let method of module.ModuleMethods){
    //         for (let option of method.Options){
    //             if (!module.ModuleOptionExist(option.Name))
    //                 module.ModuleOptions.push(option);
    //         }
    //     }
    //     for (let modelOption of module.ModuleOptions){
    //         modelOption.Required = true;
    //         for (let method of module.ModuleMethods){
    //             let contains = false;
    //             for (let methodOption of method.Options){
    //                 if (methodOption.Name == modelOption.Name){
    //                     contains = true;
    //                     break
    //                 }
    //
    //             }
    //             if (!contains) {
    //                 modelOption.Required = false;
    //                 break;
    //             }
    //         }
    //     }
    // }
    // private GetBasicCRUDUrl(methods: any[]): string {
    //     let baseUrl: string = "";
    //
    //     // find base CRUD URL it will be used to classify get methods
    //     for (let method of methods)
    //     {
    //         if (method.requests[0].protocol.http.method !== undefined) {
    //             let httpMethod = method.requests[0].protocol.http.method;
    //             if (httpMethod == 'put' || httpMethod == 'patch' || httpMethod == 'delete') {
    //                 if (method.requests[0].protocol.http.path !== undefined) {
    //                     baseUrl = method.requests[0].protocol.http.path;
    //                     break;
    //                 }
    //             }
    //         }
    //     }
    //
    //     return baseUrl;
    // }
    //
    // private AddMethod(method:any, module:Module)
    // {
    //     var moduleMethod = new ModuleMethod();
    //     let name = method.language.default.name;
    //     moduleMethod.Name = name;
    //
    //     // this._log("     method" + name );
    //     if (method.requests[0].protocol != undefined && method.requests[0].protocol.http != undefined) {
    //         moduleMethod.Url = (method.requests[0].protocol.http.path != undefined) ? method.requests[0].protocol.http.path : "";
    //         moduleMethod.HttpMethod = (method.requests[0].protocol.http.method != undefined) ? method.requests[0].protocol.http.method : "";
    //     }
    //     moduleMethod.ApiVersion = method.apiVersions[0].version;
    //
    //     // moduleMethod.Kind = this.ClassifyMethod(moduleMethod, module.BasicURL);
    //
    //     for (var p of method.parameters)
    //     {
    //         let option: ModuleOption = this.LoadModuleOption(p);
    //         if (option != undefined) {
    //             // // this._log("             add option:" + option.NameAnsible );
    //             // if (option.Kind === ModuleOptionKind.MODULE_OPTION_PATH)
    //             // {
    //             //     let splittedId: string[] = moduleMethod.Url.split("/{" + option.NameSwagger + '}');
    //             //
    //             //     if (splittedId.length == 2)
    //             //     {
    //             //         option.IdPortion = splittedId[0].split('/').pop();
    //             //     }
    //             //     else
    //             //     {
    //             //         this._log("ERROR: COULDN'T EXTRACT ID PORTION");
    //             //         splittedId.forEach(element => {
    //             //             this._log(" ... part: " + element);
    //             //         });
    //             //         this._log(" ... {" + option.NameSwagger + "}");
    //             //         this._log(" ... " + moduleMethod.Url);
    //             //     }
    //             //
    //             //     /* ajust path option schema name. */
    //             //     let name = option.NameSwagger;
    //             //     if (this.needTrimPackageName(option, moduleMethod.Url, module)) {
    //             //         name = TrimPackageName(TrimPackageName(pascalCase(option.NameSwagger), this._cliName.toLowerCase()), TrimPluralName(module.NameSwagger));
    //             //     }
    //             //     if (this._validMethodKind.has(moduleMethod.Kind)) {
    //             //         /* ajust it to resource name if it is the last part of the url. */
    //             //         if (moduleMethod.Url.endsWith("/{" + option.NameSwagger + '}')) {
    //             //             name = "name";
    //             //         }
    //             //
    //             //     }
    //             //     option.SetSchemaName(ToSnakeCase(name));
    //             // }
    //             moduleMethod.Options.push(option);
    //             if (option.Required)
    //             {
    //                 moduleMethod.RequiredOptions.push(option);
    //             }
    //         }
    //
    //     }
    //
    //     /* load body requests. */
    //     if (method.requests[0].parameters !== undefined) {
    //         moduleMethod.HasBody = true;
    //         for (var p of method.requests[0].parameters) {
    //             let option: ModuleOption = this.LoadModuleOption(p);
    //             if (option == undefined)
    //                 continue;
    //             moduleMethod.Options.push(option);
    //             if (option.Required)
    //             {
    //                 moduleMethod.RequiredOptions.push(option);
    //             }
    //
    //         }
    //     }else {
    //         moduleMethod.HasBody = false;
    //     }
    //     /* sort the request option according to the type: in-path, in-body, in-header */
    //     //moduleMethod.Options.sort((n1, n2) => n1.Kind - n2.Kind);
    //     // moduleMethod.Options.sort((n1, n2) => ((n1.Required ? 1 : 0) - (n2.Required ? 1:0)));
    //
    //     // moduleMethod.IsAsync = false; //Get the value from model 4.
    //     // if (method.extensions !== undefined && method.extensions["x-ms-long-running-operation"] !== undefined) {
    //     //     moduleMethod.IsAsync = method.extensions["x-ms-long-running-operation"];
    //     // }
    //     // moduleMethod.Documentation = (method.language.default.description != undefined) ? method.language.default.description: "";
    //     //
    //     // for (var p of method.responses) {
    //     //     if (p.schema == undefined) continue;
    //     //     if (!ContainOptionByName(p.language.default.name,p.schema.language.default.name, moduleMethod.RequiredOptions)) {
    //     //         let responseoption :TFModuleOption = this.LoadModuleOption(p, true);
    //     //         if (responseoption != undefined) {
    //     //             moduleMethod.ResponseOptions.push(responseoption);
    //     //         }
    //     //     }
    //     // }
    //     //
    //     // moduleMethod.Timeout = this.GetMethodDefaultTimeout(moduleMethod.Kind);
    //     //
    //     // this.ClassifyComputed(moduleMethod);
    //     //
    //     // /* add examples. */
    //     // if (method.extensions !== undefined && method.extensions["x-ms-examples"] !== undefined) {
    //     //     this._log("add examples");
    //     //     for (let key in method.extensions["x-ms-examples"]) {
    //     //         moduleMethod.Examples.push(method.extensions["x-ms-examples"][key]);
    //     //     }
    //     // }
    //     //
    //     // moduleMethod.SetDiscriminateBaseOptions();
    //     // if (moduleMethod.Kind === TFModuleMethodKind.MODULE_METHOD_CREATE) {
    //     //     let containedBase:Set<string> = new Set<string>();
    //     //     for (let base of moduleMethod.DiscriminatorBaseOptions) {
    //     //         if (containedBase.has(base.NameInModelSchema)) continue;
    //     //         let moduleDiscriminateConfig = new TFModuleDiscriminateConfig(base.NameInModelSchema);
    //     //         for (let dis of base.Discriminator.EnumValues) {
    //     //             if (base.GetChild(dis.Value) !== null) {
    //     //                 moduleDiscriminateConfig.DiscriminatorValues.push(dis.Value);
    //     //                 this._log("add discriminator value " + dis.Key + " of base " + base.NameInModelSchema + " to " + module.NameSwagger);
    //     //             }
    //     //         }
    //     //         base.NeedSeparated = module.NeedSeparated;
    //     //         module.Discrminates.push(moduleDiscriminateConfig);
    //     //         containedBase.add(base.NameInModelSchema);
    //     //     }
    //     //     if (moduleMethod.DiscriminatorBaseOptions.length > 0) module.Polymorphism = true;
    //     // }
    //
    //     module.ModuleMethods.push(moduleMethod);
    // }
    //
    // private LoadModuleOption(p: any, isResponse:boolean = false): ModuleOption {
    //     return this.LoadTopLevelOption(p, isResponse, this.IsAnsibleIgnoredOption);
    // }
    //
    // private LoadTopLevelOption(p: any, isResponse:boolean = false, filterFunction: (name: string) => (boolean)): ModuleOption {
    //     let option = this.LoadOption(p, isResponse, filterFunction);
    //     if (option === undefined) return undefined;
    //     return option;
    // }
    //
    // private LoadOption(p: any, isResponse:boolean = false, filterFunction: (name: string) => (boolean), parent: ModuleOption = null): ModuleOption {
    //     let name = p.language.default.name;
    //     if (filterFunction(name)) return undefined;
    //     let serializedName = p.language.default.serializedName;
    //     let extensions:any = p.extensions;
    //     let required = p.required != undefined ? p.required : false;
    //     let description = p.language.default.description;
    //
    //     let option: any;
    //     let targetschema = p.schema;
    //     let type = p.schema.type;
    //     // if (type === SwaggerModelType.SWAGGER_MODEL_ARRAY || type === SwaggerModelType.SWAGGER_MODEL_DICTIONARY) {
    //     //     targetschema = p.schema.elementType;
    //     // }
    //
    //     option = new ModuleOption(name);
    //
    //
    //     option.DispositionSdk = "*";
    //     option.NameAnsible = ToSnakeCase(name);
    //     // if (targetschema !== undefined && targetschema.discriminator !== undefined) {
    //     //     option = new TFDiscriminatorBaseOption(name);
    //     //     this._log("create TFDiscriminatorBaseOption " + name);
    //     // } else {
    //     //     option = new TFModuleOption(name);
    //     // }
    //
    //     option.Required = required;
    //     option.Documentation = description;
    //     option.Type = ParseType(type);
    //     if (parent !== null) {
    //         option.SwaggerPath = option.SwaggerPath.concat(parent.SwaggerPath);
    //     }
    //     option.SwaggerPath.push(name);
    //
    //     option.Updatable = true;
    //     if (p.readOnly != undefined) {
    //         option.Updatable = !p.readOnly;
    //         option.Computed = option.Readonly;
    //     }
    //     if (isResponse) {
    //         option.Kind = ModuleOptionKind.MODULE_OPTION_RESPONSE;
    //     } else {
    //         if (p.protocol != undefined && p.protocol.http != undefined && p.protocol.http.in != undefined) {
    //             let location = p.protocol.http.in;
    //             if (location == "url") {
    //                 option.Kind = ModuleOptionKind.MODULE_OPTION_PATH;
    //             } else if (location == "path") {
    //                 option.Kind = ModuleOptionKind.MODULE_OPTION_PATH;
    //                 option.IncludeInArgSpec = true;
    //             } else if (location == "body") {
    //                 option.Kind = ModuleOptionKind.MODULE_OPTION_BODY;
    //                 this.GetDisposition(option, parent);
    //                 option.IncludeInArgSpec = true;
    //             } else if (location == "header") {
    //                 option.Kind = ModuleOptionKind.MODULE_OPTION_HEADER;
    //             } else if (location === "query") {
    //                 option.Kind = ModuleOptionKind.MODULE_OPTION_QUERY;
    //             } else {
    //                 option.Kind = ModuleOptionKind.MODULE_OPTION_PATH;
    //                 option.IncludeInArgSpec = true;
    //             }
    //         } else {
    //             option.Kind = ModuleOptionKind.MODULE_OPTION_BODY;
    //             this.GetDisposition(option, parent);
    //             option.IncludeInArgSpec = true;
    //         }
    //     }
    //
    //     if (p.implementation != undefined) {
    //         option.Implementation = p.implementation;
    //     }
    //
    //     if (p.schema != undefined && p.schema.properties != undefined){
    //         for (let subParameter of p.schema.properties){
    //             let subOption = this.LoadOption(subParameter,isResponse, filterFunction, option);
    //             option.SubOptions.push(subOption);
    //         }
    //     }
    //
    //     if (p.schema != undefined && p.schema.type == SwaggerModelType.SWAGGER_MODEL_ARRAY){
    //         let subOption = this.LoadOption(p.schema.elementType,isResponse, filterFunction, option);
    //         option.SubOptions.push(subOption);
    //     }
    //     // if (p.schema != undefined) {
    //     //     this.LoadSchema(p.schema, option, filterFunction, isResponse);
    //     // } else {
    //     //     this._log("no schema for option " + name);
    //     // }
    //
    //
    //
    //
    //     // option.SetSchemaName(ToSnakeCase(name));
    //     // this.ClassifyOptionSchemaType(p.schema, option);
    //     //
    //     // option.ExpandFunc = this.GetOptionExpandFunc(option.Type);
    //     // option.ValidateFunc = this.GetOptionValidateFunc(option.Type)
    //     //
    //     // if (option.IsBase && option instanceof TFDiscriminatorBaseOption) {
    //     //     this.AdjustDerivedOptionNames(option);
    //     //     let typename = option.GoTypeName;
    //     //     if (option.IsList || option.IsMap) {
    //     //         typename = option.ItemGoTypeName;
    //     //     }
    //     //     option.InterfaceName = "Basic" + Capitalize(typename);
    //     // }
    //
    //     return option;
    //
    // }
    //
    // private IsAnsibleIgnoredOption(name: string) : boolean
    // {
    //     let ignoreOptions = new Set(['Apiversion','SubscriptionId', 'ApiVersion','subscriptionId', 'content_type','ContentType']);
    //     return name.indexOf('$') != -1 ||name.indexOf('_') != -1 || ignoreOptions.has(name);
    // }
    //
    // // private needTrimPackageName(option: ModuleOption, url: string, module: AnsibleCodeModel): boolean {
    // //     if (TrimPackageName(TrimPackageName(pascalCase(option.NameSwagger), this._cliName.toLowerCase()), TrimPluralName(module.NameSwagger)).toLowerCase() === 'name'.toLowerCase()
    // //         && !url.endsWith('/{' + option.NameSwagger + '}')) {
    // //         return false;
    // //     }
    // //     return true;
    // // }
    // // private LoadSchema(schema: any, option:any, filterFunction: (name: string) => (boolean), isResponse:boolean = false) {
    // //     let type = schema.type;
    // //     let itemtype = "";
    // //     let precision = null;
    // //     if (schema.precision != undefined) {
    // //         precision = schema.precision;
    // //     }
    // //
    // //     if (type === SwaggerModelType.SWAGGER_MODEL_ARRAY) {
    // //         if (schema.elementType.type.endsWith(SwaggerModelType.SWAGGER_MODEL_ENUM)) {
    // //             itemtype = schema.elementType.choiceType.type;
    // //         } else {
    // //             itemtype = schema.elementType.type;
    // //         }
    // //         // if (schema.elementType.precision != undefined) {
    // //         //     precision = schema.precision;
    // //         // }
    // //         if (itemtype === SwaggerModelType.SWAGGER_MODEL_OBJECT) {
    // //             if (this._compositeTypes != null) this._compositeTypes.push(option);
    // //         } else if (itemtype === SwaggerModelType.SWAGGER_MODEL_ENUM) {
    // //             if (this._enumTypes !== null ) this._enumTypes.push(option);
    // //         }
    // //         option.IsList = true;
    // //     }
    // //     else if (type === SwaggerModelType.SWAGGER_MODEL_DICTIONARY) {
    // //         itemtype = schema.elementType.type;
    // //         // if (schema.elementType.precision != undefined) {
    // //         //     precision = schema.precision;
    // //         // }
    // //         option.IsMap = true;
    // //     } else if (type === SwaggerModelType.SWAGGER_MODEL_CONSTENT) {
    // //         itemtype = schema.valueType.type;
    // //         // treat string constant as enum
    // //         if (itemtype === SwaggerModelType.SWAGGER_MODEL_STRING) {
    // //             type = SwaggerModelType.SWAGGER_MODEL_ENUM;
    // //             option.EnumValues = this.TF_Type_EnumValues(schema);
    // //             if (this._enumTypes !== null ) this._enumTypes.push(option);
    // //         }
    // //     } else if ( type.endsWith(SwaggerModelType.SWAGGER_MODEL_ENUM)) {
    // //         // enum type
    // //         option.EnumValues = this.TF_Type_EnumValues(schema);
    // //         itemtype = schema.choiceType.type;
    // //         if (this._enumTypes !== null ) this._enumTypes.push(option);
    // //     } else if (type === SwaggerModelType.SWAGGER_MODEL_OBJECT) {
    // //         if (this._compositeTypes != null) this._compositeTypes.push(option);
    // //     }
    // //
    // //     if (this.IsNumber(type)) {
    // //         let precision = schema.precision;
    // //         type = this.GetNumberType(type, precision);
    // //     }
    // //     if (this.IsNumber(itemtype)) {
    // //         itemtype = this.GetNumberType(schema.elementType.type, schema.elementType.precious);;
    // //     }
    // //
    // //     option.Type = type;
    // //     option.ItemType = itemtype;
    // //     option.precision = precision;
    // //     option.NameInModelSchema = schema.language.default.name;
    // //
    // //     if (schema.defaultValue != undefined) {
    // //         option.DefaultValue = schema.defaultValue;
    // //         if (type.endsWith(SwaggerModelType.SWAGGER_MODEL_ENUM)) {
    // //             for (let ev of option.EnumValues) {
    // //                 if (ev.Value === option.DefaultValue) {
    // //                     option.DefaultValue = ev.GoEnumMemberName;
    // //                 }
    // //             }
    // //         }
    // //     }
    // //
    // //     /*Get constrains */
    // //     if (schema.maxLength !== undefined || schema.minLength !== undefined || schema.pattern !== undefined ||
    // //         schema.maximum !== undefined || schema.minimum !== undefined) {
    // //         option.HasConstrains = true;
    // //
    // //         if (schema.maxLength !== undefined) option.MaxLength = schema.maxLength;
    // //         if (schema.minLength !== undefined) option.MinLength = schema.minLength;
    // //         if (schema.maximum !== undefined) option.MaxValue = schema.maximum;
    // //         if (schema.minimum !== undefined) option.MinValue = schema.minimum;
    // //         if (schema.pattern !== undefined) option.Patten = schema.pattern;
    // //
    // //         /*insert the option to the validation list. */
    // //         //PutToList(option, validate_option_list, validate_option_go_type_name_set);
    // //     }
    // //     if (type === SwaggerModelType.SWAGGER_MODEL_OBJECT || ((option.IsList || option.IsMap) && option.ItemType == SwaggerModelType.SWAGGER_MODEL_OBJECT)) {
    // //         /* add sub options. */
    // //         option.SubOptions = [];
    // //         let targetschema = schema;
    // //         if (option.IsList || option.IsMap) {
    // //             targetschema = schema.elementType;
    // //         }
    // //         /*add object parent. */
    // //         let parents = targetschema.parents;
    // //         this.LoadParent(parents, option, filterFunction);
    // //         this.LoadSubOptions(targetschema, option, filterFunction);
    // //
    // //         /*pop-up readonly metadata up. */
    // //         let popup:boolean = true;
    // //         for (let sub of option.SubOptions) {
    // //             if (!sub.ReadOnly) {
    // //                 popup = false;
    // //                 break;
    // //             }
    // //         }
    // //         if (popup && !option.IsBase) {
    // //             option.ReadOnly = true;
    // //         }
    // //     }
    // //
    // //     /* load Discriminator if any */
    // //     let targetschema = schema;
    // //     if (option.IsList || option.IsMap) {
    // //         targetschema = schema.elementType;
    // //     }
    // //     if (targetschema.discriminator !== undefined && targetschema.discriminator.all !== undefined) {
    // //         /* load discriminator. */
    // //         option.Discriminator = option.GetSubOption(targetschema.discriminator.property.language.default.name) as TFModuleOption;
    // //         option.Discriminator.Required = true;
    // //         option.Children = [];
    // //         let allderived = targetschema.discriminator.all;
    // //         let deriveds = Object.keys(allderived);
    // //         if (option.Discriminator as TFModuleOption && !option.Discriminator.Type.endsWith(SwaggerModelType.SWAGGER_MODEL_ENUM)) {
    // //             /*retrieve discriminator value from discriminator block. */
    // //             option.Discriminator.Type = SwaggerModelType.SWAGGER_MODEL_ENUM;
    // //             option.Discriminator.ItemType = SwaggerModelType.SWAGGER_MODEL_STRING;
    // //             option.Discriminator.ItemGoTypeName = ToGoCase(option.Discriminator.NameSwagger);
    // //             option.Discriminator.ItemSchemaType = this.GetOptionType(SwaggerModelType.SWAGGER_MODEL_STRING, "", TFModuleOptionTypeKind.MODULE_OPTION_TYPE_SCHEMA);
    // //             option.Discriminator.ExpandFunc = this.GetOptionExpandFunc(option.Discriminator.Type);
    // //             option.Discriminator.ValidateFunc = this.GetOptionValidateFunc(option.Discriminator.Type);
    // //             option.Discriminator.EnumValues = [];
    // //             for (let derivedName of deriveds) {
    // //                 let ev:EnumValue = new EnumValue();
    // //                 ev.Key = derivedName;
    // //                 ev.GoEnumMemberName =ToGoCase(derivedName);
    // //                 ev.Value = derivedName;
    // //                 option.Discriminator.EnumValues.push(ev);
    // //             }
    // //             if (this._enumTypes !== null ) this._enumTypes.push(option.Discriminator);
    // //         }
    // //
    // //
    // //         for (let derivedName of deriveds) {
    // //             if (option instanceof TFDiscriminatorBaseOption) {
    // //                 let derivedOption = this.LoadDerivedOption(allderived[derivedName], option, filterFunction);
    // //                 if (derivedOption !== null) {
    // //                     option.Children.push(derivedOption);
    // //                 }
    // //             }
    // //         }
    // //     }
    // // }
    //
    // private GetDisposition(option: ModuleOption, parent: ModuleOption = null){
    //
    //     if (parent == null){
    //         if (option.NameSwagger == 'location' || option.NameSwagger =='tags' ||
    //             option.NameSwagger == 'identity' ||  option.NameSwagger == 'sku'){
    //             option.DispositionRest =  "/"+option.NameSwagger;
    //         }
    //         else
    //             option.DispositionRest =  "/properties/"+option.NameSwagger;
    //         option.DispositionSdk = "/"+ToSnakeCase(option.NameSwagger);
    //     }else {
    //         option.DispositionSdk = ToSnakeCase(option.NameSwagger);
    //         option.DispositionRest =   option.NameSwagger;
    //     }
    //
    // }
}

