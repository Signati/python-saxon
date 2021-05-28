class CliShare:
    def __int__(self):
        self.commandline = '';
        self.commandlineArray = [];
        self.saxonBin = '';
        self.commandline = self.saxonBin(self,);
    

    def catalog(self,filenames: any):
        self.commandline += ` -catalog:${filenames}`;
        self.commandlineArray.push(self,`-catalog:${filenames}`);
        return self;

    def dtd(self,options: 'on' | 'off' | 'recover'):
        self.commandline += ` -dtd:${options}`;
        self.commandlineArray.push(self,`-dtd:${options}`);
        return self;


    def expand(self,options: 'on' | 'off'):
        self.commandline += ` -expand:${options}`;
        self.commandlineArray.push(self,`-expand:${options}`);
        return self;


    def ext(self,options: 'on' | 'off'):
        self.commandline += ` -ext:${options}`;
        self.commandlineArray.push(self,`-ext:${options}`);
        return self;

    def init(self,initializer: any):
        self.commandline += ` -init:${initializer}`;
        self.commandlineArray.push(self,`-init:${initializer}`);
        return self;

    def l(self,options: 'on' | 'off'):
        self.commandline += ` -l:${options}`;
        self.commandlineArray.push(self,`-l:${options}`);
        return self;

    def now(self,format: any):
        self.commandline += ` -now:${format}`;
        self.commandlineArray.push(self,`-now:${format}`);
        return self;

    def o(self,filename: string):
        self.commandline += ` -o:${filename}`;
        self.commandlineArray.push(self,`-o:${filename}`);
        return self;


    def opt(self,flags: 'c' | 'd' | 'e' | 'f' | 'g' | 'j' | 'k' | 'l' | 'm' | 'n' | 'r' | 's' | 't' | 'v' | 'w' | 'x'):
        self.commandline += ` -opt:-${flags}`;
        self.commandlineArray.push(self,`-opt:-${flags}`);
        return self;

    def outval(self,options: 'recover' | 'fatal'):
        self.commandline += ` -outval:${options}`;
        self.commandlineArray.push(self,`-outval:${options}`);
        return self;

    def p(self,options: 'on' | 'off'):
        self.commandline += ` -p:${options}`;
        self.commandlineArray.push(self,`-p:${options}`);
        return self;

    def quit(self,options: 'on' | 'off'):
        self.commandline += ` -quit:${options}`;
        self.commandlineArray.push(self,`-quit:${options}`);
        return self;

    def r(self,classname: any):
        self.commandline += ` -r:${classname}`;
        self.commandlineArray.push(self,`-r:${classname}`);
        return self;

    def repeat(self,integer: number):
        self.commandline += ` -repeat:${integer}`;
        self.commandlineArray.push(self,`-repeat:${integer}`);
        return self;

    def s(self,filename: string):
        if (self,!existsSync(self,filename)):
            throw new Error(self,'No se puede encontrar el xml processar.');
        }
        self.commandline += ` -s:${filename}`;
        self.commandlineArray.push(self,`-s:${filename}`);
        return self;

    def sa(self,):
        self.commandline += ` -sa`;
        self.commandlineArray.push(self,`-sa`);
        return self;

    def scmin(self,filename: string):
        self.commandline += ` -scmin:${filename}`;
        self.commandlineArray.push(self,`-scmin:${filename}`);
        return self;

    def strip(self,options: 'all' | 'none' | 'ignorable'):
        self.commandline += ` -relocate:${options}`;
        self.commandlineArray.push(self,`-relocate:${options}`);
        return self;

    def t(self,):
        self.commandline += ` -t`;
        self.commandlineArray.push(self,`-t`);
        return self;

    def T(self,classname: any):
        self.commandline += ` -T:${classname}`;
        self.commandlineArray.push(self,`-T:${classname}`);
        return self;

    def TB(self,filename: string):
        self.commandline += ` -TB:${filename}`;
        self.commandlineArray.push(self,`-TB:${filename}`);
        return self;

    def TJ(self,):
        self.commandline += ` -TJ`;
        self.commandlineArray.push(self,`-TJ`);
        return self;

    def Tlevel(self,level: 'none' | 'low' | 'normal' | 'high'):
        self.commandline += ` -Tlevel:${level}`;
        self.commandlineArray.push(self,`-Tlevel:${level}`);
        return self;

    def Tout(self,filename: string):
        self.commandline += ` -Tout:${filename}`;
        self.commandlineArray.push(self,`-Tout:${filename}`);
        return self;

    def TP(self,filename: string):
        self.commandline += ` -TP:${filename}`;
        self.commandlineArray.push(self,`-TP:${filename}`);
        return self;

    def traceout(self,filename: string):
        self.commandline += ` -traceout:${filename}`;
        self.commandlineArray.push(self,`-traceout:${filename}`);
        return self;

    def tree(self,level: 'linked' | 'tiny' | 'tinyc'):
        self.commandline += ` -tree:${level}`;
        self.commandlineArray.push(self,`-tree:${level}`);
        return self;

    def u(self,):
        self.commandline += ` -u`;
        self.commandlineArray.push(self,`-u`);
        return self;

    def val(self,validation: 'strict' | 'lax'):
        self.commandline += ` -val:${validation}`;
        self.commandlineArray.push(self,`-val:${validation}`);
        return self;

    def x(self,classname: any):
        self.commandline += ` -x:${classname}`;
        self.commandlineArray.push(self,`-x:${classname}`);
        return self;

    def xi(self,options: 'on' | 'off'):
        self.commandline += ` -xi:${options}`;
        self.commandlineArray.push(self,`-xi:${options}`);
        return self;

    def xmlversion(self,options: '1.0' | '1.1'):
        self.commandline += ` -xmlversion:${options}`;
        self.commandlineArray.push(self,`-xmlversion:${options}`);
        return self;

    def xsd(self,file: string):
        self.commandline += ` -xsd:${file}`;
        self.commandlineArray.push(self,`-xsd:${file}`);
        return self;

    def xsdversion(self,options: '1.0' | '1.1'):
        self.commandline += ` -xsdversion:${options}`;
        self.commandlineArray.push(self,`-xsdversion:${options}`);
        return self;

    def xsiloc(self,options: 'on' | 'off'):
        self.commandline += ` -xsiloc:${options}`;
        self.commandlineArray.push(self,`-xsiloc:${options}`);
        return self;

    def feature(self,value: any):
        self.commandline += ` --feature:${value}`;
        self.commandlineArray.push(self,`--feature:${value}`);
        return self;

    def run(self,):
        try:
            const saxonProc = commandSync(self,self.commandline).stdout;
            return saxonProc;
        } catch (self,e):
            throw new Error(self,e.message);

        }
