import {ModuleExample} from "./ModuleExample";
import * as yaml from "node-yaml";
import {ModuleMethod} from "./ModuleMethod";
import {ModuleOption, ModuleOptionKind} from "./ModuleOption";
import {SwaggerModelType} from "../../utils/helper";
export class Test{
    public ModuleName: string = null;
    public ModuleMethods: ModuleMethod[] = [];
    public ParameterValues: Map<string, any> = new Map<string, any>();
    public Examples: any[] = [];
    public ObjectName: string;
    constructor(moduleName: string, moduleMethods: ModuleMethod[], objectName: string) {
        this.ModuleName = moduleName;
        this.ModuleMethods = moduleMethods;
        this.ObjectName = objectName;
        // this.Init();
    }
    // Init(){
    //     for (let method of this.ModuleMethods){
    //         for (let parameter of method.Options){
    //             this.GetParameter(parameter);
    //         }
    //     }
    //     this.GetExample(new Set(["create", "create_or_update"]), "Create a " + this.ObjectName);
    //     this.GetExample(new Set(["get"]), "get the " + this.ObjectName );
    //     this.GetExample(new Set(["update", "create_or_update"]), "Update the " + this.ObjectName + " (no change)");
    //     this.UpdateParameters();
    //     this.GetExample(new Set(["update", "create_or_update"]), "Update the " + this.ObjectName + "");
    //     this.GetExample(new Set(["delete"]), "Delete the " + this.ObjectName);
    // }
    // UpdateParameters(){
    //     for (let method of this.ModuleMethods){
    //         for (let parameter of method.Options){
    //             if (this.ParameterValues.has(parameter.Name)  && parameter.Kind == ModuleOptionKind.MODULE_OPTION_BODY)
    //                 this.ParameterValues.set(parameter.Name, this.ParameterValues.get(parameter.Name)+"2");
    //         }
    //     }
    // }
    // GetParameter(parameter: ModuleOption){
    //     if (this.ParameterValues.has(parameter.Name))
    //         return this.ParameterValues.get(parameter.Name);
    //     let value = this.GetValue(parameter);
    //     if (value != null)
    //         this.ParameterValues.set(parameter.Name, value);
    // }
    // GetValue(parameter: ModuleOption){
    //     // need to add more situations
    //     if (parameter.SwaggerType == SwaggerModelType.SWAGGER_MODEL_STRING){
    //         return "my_"+parameter.Name;
    //     }
    //     if (parameter.SwaggerType == SwaggerModelType.SWAGGER_MODEL_BOOLEAN){
    //         return true;
    //     }
    //     return null;
    // }
    // GetExample(methodName: Set<string>, exampleName: string){
    //     let nowMethod: ModuleMethod = null;
    //     for (let method of this.ModuleMethods){
    //         if (methodName.has(method.Name)){
    //             nowMethod = method;
    //             break;
    //         }
    //     }
    //     if (nowMethod == null)
    //         return;
    //     let example = {};
    //     example['name'] = exampleName;
    //     let parameters = {};
    //     for (let parameter of nowMethod.Options){
    //         if (this.ParameterValues.has(parameter.Name)){
    //             parameters[parameter.Name] = this.ParameterValues.get(parameter.Name);
    //         }
    //     }
    //     if (methodName.has('delete'))
    //         parameters['state'] = 'absent';
    //     let content = {};
    //     if (methodName.has("get")){
    //         content[this.ModuleName +"_info"] = parameters;
    //     }else {
    //         content[this.ModuleName] = parameters;
    //     }
    //
    //     example['content'] = content;
    //
    //     this.Examples.push(example);
    // }

}