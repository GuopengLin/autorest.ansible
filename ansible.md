# autorest.ansible doc

## User Guide

### Preparation

#### 1. install the autorest 

```
npm install -g autorest 
```
**ps:** If there is not npm and node installed in your computer, you should first install them. 
	
The node and npm version in my machine:
	
```
node -v
v12.18.3
	
npm -v
6.14.6
```
other versions may work as well, please check  
	```https://github.com/Azure/autorest``` for more information about suppported versions of node 
	
After installation, please check whether the autorest runs well

```
autorest --help 
```

If there is not failure in the console , it is very lucky for you, then you can go to the next step.

But if  something wrong happens, you can first google for some solutions. And if it still doesn't work at the end, maybe you need to launch a virtural machine in the azure( or other cloud service providers) , and set up the environment in it, just like me.
	


	
#### 2. clone the api spec
```
git clone https://github.com/Azure/azure-rest-api-specs.git
```
	
#### 3. install the typescript

```
sudo npm install -g typescript
```


#### 4. clone the ansible repo 
	
``` 
git clone https://github.com/GuopengLin/autorest.ansible.git
```


#### 5. install the module dependence

```
cd [path of autorest.ansible]

npm install 

```
#### 6. compile

```
tsc -p .
```
#### 7. run

```
autorest --ansible --use=./  [path or README.md]   --ansible-output-folder=[output-dir-path]

eg:
	autorest --ansible --use=./  ~/azure-rest-api-specs/specification/compute/resource-manager/readme.md  --log --ansible-output-folder=./tmp
```

### Usage

If all the preparations have been done, now you can generate any modules you like.

Eg:
	
1. generate modules of the compute client:
	```
	autorest --ansible --use=./  ~/azure-rest-api-specs/specification/compute/resource-manager/readme.md  --log --ansible-output-folder=./tmp
	```
2. generate modules of the authorization client:
	```
	autorest --ansible --use=./  ~/azure-rest-api-specs/specification/authorization/resource-manager/readme.md  --log --ansible-output-folder=./tmp
	```
	 
There will be a azure_rm_usage or azure_rm_sku module in the tmp directory which i  think  is unuseful,but i still keep it in the code.You can choose the modules you want and delete the others.


### Questions 

1. 

```
autorest --help

(C) 2018 Microsoft Corporation.
https://aka.ms/autorest
Failure:
Error: Unable to find a valid AutoRest core package '@autorest/core' @ '~3.0.0'.
Error: Unable to find a valid AutoRest core package '@autorest/core' @ '~3.0.0'.
    at Object.selectVersion (/usr/local/lib/node_modules/autorest/dist/autorest-as-a-service.js:262:23)
    at processTicksAndRejections (internal/process/task_queues.js:97:5)
```

**solution:**
```
sudo npm install -g @autorest/core
```

2.

```
azureuser@Test2:~/autorest.ansible$ autorest --ansible --use=./  ~/azure-rest-api-specs/specification/compute/resource-manager/readme.md  --log --ansible-output-folder=./tmp
AutoRest code generation utility [cli version: 3.0.6244; node: v12.18.3, max-memory: 8192 gb]
(C) 2018 Microsoft Corporation.
https://aka.ms/autorest
   Loading AutoRest core      '/usr/local/lib/node_modules/@autorest/core/dist' (3.0.6306)
   Loading local AutoRest extension '@autorest/ansible' (/home/azureuser/autorest.ansible/)
   Installing AutoRest extension '@autorest/clicommon' (0.4.13)
Failed to install or start extension '@autorest/clicommon' (0.4.13)
  Error: Package '@autorest/clicommon' - '0.4.13' failed to install:
  Failed to install package 'https://registry.npmjs.org/@autorest/clicommon/-/clicommon-0.4.13.tgz' -- Error: Process Failed.Error: Failed to install package 'https://registry.npmjs.org/@autorest/clicommon/-/clicommon-0.4.13.tgz' -- Error: Process Failed.
    at install (/node_modules/@azure-tools/extension/dist/main.js:367:15)
    at processTicksAndRejections (internal/process/task_queues.js:97:5)
    at async ExtensionManager.installPackage (/node_modules/@azure-tools/extension/dist/main.js:571:13)
    at async resolveExtensions (/usr/local/lib/node_modules/@autorest/core/dist/lib/configuration.js:926:55)
    at async Configuration.CreateView (/usr/local/lib/node_modules/@autorest/core/dist/lib/configuration.js:967:9)
    at async AutoRest.RegenerateView (/usr/local/lib/node_modules/@autorest/core/dist/lib/autorest-core.js:66:29)
    at async currentMain (/usr/local/lib/node_modules/@autorest/core/dist/app.js:311:21)
    at async mainImpl (/usr/local/lib/node_modules/@autorest/core/dist/app.js:510:20)
    at async main (/usr/local/lib/node_modules/@autorest/core/dist/app.js:537:20)
```

**solution:**

```
sudo npm install -g @autorest/clicommon
```

3.

```
azureuser@Test2:~/autorest.ansible$ autorest --ansible --use=./  ~/azure-rest-api-specs/specification/authorization/resource-manager/readme.md  --log --ansible-output-folder=./tmp
AutoRest code generation utility [cli version: 3.0.6244; node: v12.18.3, max-memory: 8192 gb]
(C) 2018 Microsoft Corporation.
https://aka.ms/autorest
   Loading AutoRest core      '/usr/local/lib/node_modules/@autorest/core/dist' (3.0.6306)
   Loading local AutoRest extension '@autorest/ansible' (/home/azureuser/autorest.ansible/)
   Loading local AutoRest extension '@autorest/clicommon' (/usr/local/lib/node_modules/@autorest/clicommon)
   Installing AutoRest extension '@autorest/modelerfour' (4.15.378)
Failed to install or start extension '@autorest/modelerfour' (4.15.378)
  Error: Package '@autorest/modelerfour' - '4.15.378' failed to install:
  Failed to install package 'https://github.com/Azure/autorest.modelerfour/releases/download/v4.15.378/autorest-modelerfour-4.15.378.tgz' -- Error: Process Failed.Error: Failed to install package 'https://github.com/Azure/autorest.modelerfour/releases/download/v4.15.378/autorest-modelerfour-4.15.378.tgz' -- Error: Process Failed.
    at install (/node_modules/@azure-tools/extension/dist/main.js:367:15)
    at processTicksAndRejections (internal/process/task_queues.js:97:5)
    at async ExtensionManager.installPackage (/node_modules/@azure-tools/extension/dist/main.js:571:13)
    at async resolveExtensions (/usr/local/lib/node_modules/@autorest/core/dist/lib/configuration.js:926:55)
    at async Configuration.CreateView (/usr/local/lib/node_modules/@autorest/core/dist/lib/configuration.js:967:9)
    at async AutoRest.RegenerateView (/usr/local/lib/node_modules/@autorest/core/dist/lib/autorest-core.js:66:29)
    at async currentMain (/usr/local/lib/node_modules/@autorest/core/dist/app.js:311:21)
    at async mainImpl (/usr/local/lib/node_modules/@autorest/core/dist/app.js:510:20)
    at async main (/usr/local/lib/node_modules/@autorest/core/dist/app.js:537:20)

```


**solution:**

```
sudo npm install -g @autorest/modelerfour --unsafe-perm
```

## Developer Guide

### 1. preparation

I have to assume that you have konwn about how to use the autorest.ansible to generate modules.

If so, you can go to the next step.


