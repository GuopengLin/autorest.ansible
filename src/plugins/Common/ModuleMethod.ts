import {ModuleOption, ModuleOptionKind} from "./ModuleOption";
import {ToSnakeCase} from "../../utils/helper";

export class ModuleMethod {
    constructor(objectName: string,swaggerMethod: any) {
        this.ModuleObjectName = objectName;
        this.Init(swaggerMethod);
    }

    private Init(swaggerMethod: any){
        this.Name = swaggerMethod.language.default.name;
        if (swaggerMethod.requests[0].protocol != undefined && swaggerMethod.requests[0].protocol.http != undefined) {
            this.Url = (swaggerMethod.requests[0].protocol.http.path != undefined) ? swaggerMethod.requests[0].protocol.http.path : "";
            this.HttpMethod = (swaggerMethod.requests[0].protocol.http.method != undefined) ? swaggerMethod.requests[0].protocol.http.method : "";
        }
        this.LoadOption(swaggerMethod.parameters);
        if (swaggerMethod.requests[0].parameters !== undefined) {
            for (let parameter of swaggerMethod.requests[0].parameters) {
                if (!this.IsAnsibleIgnoredOption(parameter.language.default.name)){
                    this.ParameterName = ToSnakeCase(parameter.language.default.name);
                    this.LoadOption(parameter.schema.properties);
                    break;
                }
            }
            this.HasBody = true;
        }else
            this.HasBody = false;
        if (swaggerMethod.responses[0].schema != null){
            if (swaggerMethod.responses[0].schema.parents != null && swaggerMethod.responses[0].schema.parents.all != null)
                this.LoadResponseOption(swaggerMethod.responses[0].schema.parents.all[0].properties);
            if (swaggerMethod.responses[0].schema.properties != null)
                this.LoadResponseOption(swaggerMethod.responses[0].schema.properties);
        }
    }

    private LoadOption(parameters: any){
        for (let parameter of parameters){
            let option = new ModuleOption(this.ModuleObjectName, parameter, null, false, new Set<string>());
            if (this.IsAnsibleIgnoredOption(option.Name))
                continue;
            if (option.ReadOnly)
                continue;
            this.Options.push(option);
            if (option.Required){
                this.RequiredOptions.push(option);
            }
        }
    }

    private LoadResponseOption(parameters: any){
        for (let parameter of parameters){
            let option = new ModuleOption(this.ModuleObjectName, parameter, null, true, new Set<string>());
            this.ResponseOptions.push(option);
        }
    }

    private IsAnsibleIgnoredOption(name: string) : boolean
    {
        let ignoreOptions = new Set(['Apiversion','SubscriptionId', 'ApiVersion','subscriptionId', 'content_type','ContentType','api_version', 'subscription_id']);
        return name.indexOf('$') != -1  || ignoreOptions.has(name);
    }

    public GetOption(name: string){
        for (let option of this.Options){
            if (option.Name == name)
                return option;
        }
        return null;
    }
    public Name: string = null;
    public Options: ModuleOption[] = [];
    public ModuleObjectName: string;
    public RequiredOptions: ModuleOption[] = [];
    public ResponseOptions: ModuleOption[] = [];
    public Url: string = "";
    public SwaggerMethod: any;
    public HttpMethod: string = "";
    public ApiVersion: string = "";
    public HasBody: boolean = false;
    public ParameterName: string = "parameters";
}
