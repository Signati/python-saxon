class Transform(CliShare):
    def __init__(self):
        self.commandline = '';
        self.commandlineArray= [];
        self.saxonBin = '';
        self.saxonBin = self.getOS();
        self.commandline = self.saxonBin

    def a(self,options: 'on' | 'off'):
        self.commandline += ` -a:${options}`;
        self.commandlineArray.push(self,`-a:${options}`);
        return self;

    def ea(self,options: 'on' | 'off'):
        self.commandline += ` -ea:${options}`;
        self.commandlineArray.push(self,`-ea:${options}`);
        return self;

    def explain(self,filename: any):
        self.commandline += ` -explain:${filename}`;
        self.commandlineArray.push(self,`-explain:${filename}`);
        return self;

    def export(self,filename: any):
        self.commandline += ` -export:${filename}`;
        self.commandlineArray.push(self,`-export:${filename}`);
        return self;

    def im(self,modename: any):
        self.commandline += ` -im:${modename}`;
        self.commandlineArray.push(self,`-im:${modename}`);
        return self;

    def it(self,template: any):
        self.commandline += ` -it:${template}`;
        self.commandlineArray.push(self,`-it:${template}`);
        return self;


    def jit(self,options: 'on' | 'off'):
        self.commandline += ` -jit:${options}`;
        self.commandlineArray.push(self,`-jit:${options}`);
        return self;


    def lib(self,filenames: any):
        self.commandline += ` -lib:${filenames}`;
        self.commandlineArray.push(self,`-lib:${filenames}`);
        return self;

    def license(self,options: 'on' | 'off'):
        self.commandline += ` -license:${options}`;
        self.commandlineArray.push(self,`-license:${options}`);
        return self;

    def m(self,classname: any):
        self.commandline += ` -m:${classname}`;
        self.commandlineArray.push(self,`-m:${classname}`);
        return self;

    def nogo(self,):
        self.commandline += ` -nogo`;
        self.commandlineArray.push(self,`-nogo`);
        return self;

    def ns(self,options: 'uri' | '##any' | '##html5'):
        self.commandline += ` -ns:${options}`;
        self.commandlineArray.push(self,`-ns:${options}`);
        return self;

    def or(self,classname: any):
        self.commandline += ` -or:${classname}`;
        self.commandlineArray.push(self,`-or:${classname}`);
        return self;

    def relocate(self,options: 'on' | 'off'):
        self.commandline += ` -relocate:${options}`;
        self.commandlineArray.push(self,`-relocate:${options}`);
        return self;


    def target(self,target: 'EE' | 'PE' | 'HE' | 'JS'):
        self.commandline += ` -target:${target}`;
        self.commandlineArray.push(self,`-target:${target}`);
        return self;

    def threads(self,N: number):
        // todo only -S is activate
        self.commandline += ` -threads:${N}`;
        self.commandlineArray.push(self,`-threads:${N}`);
        return self;

    def warnings(self,validation: 'silent' | 'recover' | 'fatal'):
        self.commandline += ` -warnings:${validation}`;
        self.commandlineArray.push(self,`-warnings:${validation}`);
        return self;

    def xsl(self,filename: string):
        if (self,!existsSync(self,filename)):
            throw new Error(self,'No se puede encontrar el archivo para la cadena original!.');
        }
        self.commandline += ` -xsl:${filename}`;
        self.commandlineArray.push(self,`-xsl:${filename}`);
        return self;

    def y(self,filename):
        self.commandline += ` -y:${filename}`;
        self.commandlineArray.push(self,`-y:${filename}`);
        return self;


    def params(self,value: any):
        return 1

    def getOS(self):
        # if (self,platform(self,) === 'win32'):
        #     return 'transform.exe';
        # } else if (self,platform(self,) === 'linux'):
        #     return 'saxon-xslt';
        # } else if (self,platform(self,) === 'darwin'):
        #     return 'transform';
        #     // var chilkat = require(self,'@chilkat/ck-node11-macosx');
        # }
        # return 'transform';
