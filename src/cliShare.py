class CliShare:
    def __int__(self):
        self.commandline = '';
        self.commandlineArray = [];
        self.saxonBin = '';
        self.commandline = self.saxonBin(self, );

    def catalog(self, filenames: any):
        self.commandline += " -catalog:${filenames}";
        self.commandlineArray.append("-catalog:${filenames}");
        return self;

    def dtd(self, options: 'on' | 'off' | 'recover'):
        self.commandline += " -dtd:${options}";
        self.commandlineArray.append("-dtd:${options}");
        return self;

    def expand(self, options: 'on' | 'off'):
        self.commandline += " -expand:${options}";
        self.commandlineArray.append("-expand:${options}");
        return self;

    def ext(self, options: 'on' | 'off'):
        self.commandline += " -ext:${options}";
        self.commandlineArray.append("-ext:${options}");
        return self;

    def init(self, initializer: any):
        self.commandline += " -init:${initializer}";
        self.commandlineArray.append("-init:${initializer}");
        return self;

    def l(self, options: 'on' | 'off'):
        self.commandline += " -l:${options}";
        self.commandlineArray.append("-l:${options}");
        return self;

    def now(self, format: any):
        self.commandline += " -now:${format}";
        self.commandlineArray.append("-now:${format}");
        return self;

    def o(self, filename):
        self.commandline += " -o:${filename}";
        self.commandlineArray.append("-o:${filename}");
        return self;

    def opt(self, flags: 'c' | 'd' | 'e' | 'f' | 'g' | 'j' | 'k' | 'l' | 'm' | 'n' | 'r' | 's' | 't' | 'v' | 'w' | 'x'):
        self.commandline += " -opt:-${flags}";
        self.commandlineArray.append("-opt:-${flags}");
        return self;

    def outval(self, options: 'recover' | 'fatal'):
        self.commandline += " -outval:${options}";
        self.commandlineArray.append("-outval:${options}");
        return self;

    def p(self, options: 'on' | 'off'):
        self.commandline += " -p:${options}";
        self.commandlineArray.append("-p:${options}");
        return self;

    def quit(self, options: 'on' | 'off'):
        self.commandline += " -quit:${options}";
        self.commandlineArray.append("-quit:${options}");
        return self;

    def r(self, classname: any):
        self.commandline += " -r:${classname}";
        self.commandlineArray.append("-r:${classname}");
        return self;

    def repeat(self, integer):
        self.commandline += " -repeat:${integer}";
        self.commandlineArray.append("-repeat:${integer}");
        return self;

    def s(self, filename):
        # if (self,!existsSync(self, filename)):
        #     throw
        #     new
        #     Error(self, 'No se puede encontrar el xml processar.');
        # }
        self.commandline += " -s:${filename}";
        self.commandlineArray.append("-s:${filename}");
        return self;

    def sa(self, ):
        self.commandline += " -sa";
        self.commandlineArray.append("-sa");
        return self;

    def scmin(self, filename):
        self.commandline += " -scmin:${filename}";
        self.commandlineArray.append("-scmin:${filename}");
        return self;

    def strip(self, options: 'all' | 'none' | 'ignorable'):
        self.commandline += " -relocate:${options}";
        self.commandlineArray.append("-relocate:${options}");
        return self;

    def t(self, ):
        self.commandline += " -t";
        self.commandlineArray.append("-t");
        return self;

    def T(self, classname: any):
        self.commandline += " -T:${classname}";
        self.commandlineArray.append("-T:${classname}");
        return self;

    def TB(self, filename):
        self.commandline += " -TB:${filename}";
        self.commandlineArray.append("-TB:${filename}");
        return self;

    def TJ(self, ):
        self.commandline += " -TJ";
        self.commandlineArray.append("-TJ");
        return self;

    def Tlevel(self, level: 'none' | 'low' | 'normal' | 'high'):
        self.commandline += " -Tlevel:${level}";
        self.commandlineArray.append("-Tlevel:${level}");
        return self;

    def Tout(self, filename):
        self.commandline += " -Tout:${filename}";
        self.commandlineArray.append("-Tout:${filename}");
        return self;

    def TP(self, filename):
        self.commandline += " -TP:${filename}";
        self.commandlineArray.append("-TP:${filename}");
        return self;

    def traceout(self, filename):
        self.commandline += " -traceout:${filename}";
        self.commandlineArray.append("-traceout:${filename}");
        return self;

    def tree(self, level: 'linked' | 'tiny' | 'tinyc'):
        self.commandline += " -tree:${level}";
        self.commandlineArray.append("-tree:${level}");
        return self;

    def u(self, ):
        self.commandline += " -u";
        self.commandlineArray.append("-u");
        return self;

    def val(self, validation: 'strict' | 'lax'):
        self.commandline += " -val:${validation}";
        self.commandlineArray.append("-val:${validation}");
        return self;

    def x(self, classname: any):
        self.commandline += " -x:${classname}";
        self.commandlineArray.append("-x:${classname}");
        return self;

    def xi(self, options: 'on' | 'off'):
        self.commandline += " -xi:${options}";
        self.commandlineArray.append("-xi:${options}");
        return self;

    def xmlversion(self, options: '1.0' | '1.1'):
        self.commandline += " -xmlversion:${options}";
        self.commandlineArray.append("-xmlversion:${options}");
        return self;

    def xsd(self, file):
        self.commandline += " -xsd:${file}";
        self.commandlineArray.append("-xsd:${file}");
        return self;

    def xsdversion(self, options: '1.0' | '1.1'):
        self.commandline += " -xsdversion:${options}";
        self.commandlineArray.append("-xsdversion:${options}");
        return self;

    def xsiloc(self, options: 'on' | 'off'):
        self.commandline += " -xsiloc:${options}";
        self.commandlineArray.append("-xsiloc:${options}");
        return self;

    def feature(self, value: any):
        self.commandline += " --feature:${value}";
        self.commandlineArray.append("--feature:${value}");
        return self;

    def run(self, ):
        return 1
        # try:
        #     const saxonProc = commandSync(self,self.commandline).stdout;
        #     return saxonProc;
        # } catch (self,e):
        #     throw new Error(self,e.message);
        #
        # }
