
import {ModuleMethod} from "./ModuleMethod";

export class ModuleTest{
    public ModuleName: string = null;
    public ModuleMethods: ModuleMethod[] = [];
    public ParameterValues: Map<string, any> = new Map<string, any>();
    public Examples: any[] = [];
    public ObjectName: string;
    constructor(moduleName: string, moduleMethods: ModuleMethod[], objectName: string) {
        this.ModuleName = moduleName;
        this.ModuleMethods = moduleMethods;
        this.ObjectName = objectName;
    }


}