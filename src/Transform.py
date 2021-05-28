from cliShare import CliShare


class Transform(CliShare):
    def __init__(self):
        self.commandline = '';
        self.commandlineArray= [];
        self.saxonBin = '';
        self.saxonBin = self.getOS();
        self.commandline = self.saxonBin

    def a(self,options: 'on' | 'off'):
        self.commandline += " -a:${options}";
        self.commandlineArray.append("-a:${options}");
        return self;

    def ea(self,options: 'on' | 'off'):
        self.commandline += " -ea:${options}";
        self.commandlineArray.append("-ea:${options}");
        return self;

    def explain(self,filename: any):
        self.commandline += " -explain:${filename}";
        self.commandlineArray.append("-explain:${filename}");
        return self;

    def export(self,filename: any):
        self.commandline += " -export:${filename}";
        self.commandlineArray.append("-export:${filename}");
        return self;

    def im(self,modename: any):
        self.commandline += " -im:${modename}";
        self.commandlineArray.append("-im:${modename}");
        return self;

    def it(self,template: any):
        self.commandline += " -it:${template}";
        self.commandlineArray.append("-it:${template}");
        return self;


    def jit(self,options: 'on' | 'off'):
        self.commandline += " -jit:${options}";
        self.commandlineArray.append("-jit:${options}");
        return self;


    def lib(self,filenames: any):
        self.commandline += " -lib:${filenames}";
        self.commandlineArray.append("-lib:${filenames}");
        return self;

    def license(self,options: 'on' | 'off'):
        self.commandline += " -license:${options}";
        self.commandlineArray.append("-license:${options}");
        return self;

    def m(self,classname: any):
        self.commandline += " -m:${classname}";
        self.commandlineArray.append("-m:${classname}");
        return self;

    def nogo(self,):
        self.commandline += " -nogo";
        self.commandlineArray.append("-nogo");
        return self;

    def ns(self,options: 'uri' | '##any' | '##html5'):
        self.commandline += " -ns:${options}";
        self.commandlineArray.append("-ns:${options}");
        return self;

    def or(self,classname: any):
        self.commandline += " -or:${classname}";
        self.commandlineArray.append("-or:${classname}");
        return self;

    def relocate(self,options: 'on' | 'off'):
        self.commandline += " -relocate:${options}";
        self.commandlineArray.append("-relocate:${options}");
        return self;


    def target(self,target: 'EE' | 'PE' | 'HE' | 'JS'):
        self.commandline += " -target:${target}";
        self.commandlineArray.append("-target:${target}");
        return self;

    def threads(self,N):
        #// todo only -S is activate
        self.commandline += " -threads:${N}";
        self.commandlineArray.append("-threads:${N}");
        return self;

    def warnings(self,validation: 'silent' | 'recover' | 'fatal'):
        self.commandline += " -warnings:${validation}";
        self.commandlineArray.append("-warnings:${validation}");
        return self;

    def xsl(self,filename):
        # if (!existsSync(self,filename)):
        #     throw new Error(self,'No se puede encontrar el archivo para la cadena original!.');
        # }
        self.commandline += " -xsl:${filename}";
        self.commandlineArray.append("-xsl:${filename}");
        return self;

    def y(self,filename):
        self.commandline += " -y:${filename}";
        self.commandlineArray.append("-y:${filename}");
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
