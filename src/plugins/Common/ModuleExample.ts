import {ModuleMethod} from "./ModuleMethod";
import {ToSnakeCase} from "../../utils/helper";

export class ModuleExample {
    constructor(name: string, content: any, method: ModuleMethod) {
        this.Name = name;
        this.methodName = method.Name;
        this.GetParameters(content.parameters, method);
    }
    private GetParameters(swaggerParameters: any, method: ModuleMethod){
        for (let name in swaggerParameters){
            let option = method.GetOption(ToSnakeCase(name));
            if (option == null) continue;
            this.Value[ToSnakeCase(name)] = this.ParseParameter(swaggerParameters[name]);
        }
        if (method.ParameterName != null){
            let body = swaggerParameters[method.ParameterName]
            for (let name in body){
                this.Value[ToSnakeCase(name)] = this.ParseParameter(body[name]);
            }
        }
    }

    private ParseParameter(content: any):any{
        if (typeof content == "object"){
            if (content instanceof Array){
                let result = [];
                for (let element of content)
                    result.push(this.ParseParameter(element));
                return result;
            }else{
                let result = {};
                for (let name in content){
                    result[ToSnakeCase(name)] = this.ParseParameter(content[name]);
                }
                return result;
            }
        }else
            return content;
    }
    public Name: string;
    public Value: object = {};
    public methodName: string;

}
