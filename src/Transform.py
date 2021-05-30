from CliShare import CliShare
import sys


class Transform(CliShare):
    def __init__(self):
        self.commandline = '';
        self.commandlineArray = [];
        self.saxonBin = '';
        self.saxonBin = self.getOS();
        self.commandline = self.saxonBin

    # 'on' | 'off'
    def a(self, options):
        self.commandline += " -a:" + options;
        self.commandlineArray.append("-a:" + options);
        return self;

    # 'on' | 'off'
    def ea(self, options):
        self.commandline += " -ea:" + options;
        self.commandlineArray.append("-ea:" + options);
        return self;

    def explain(self, filename):
        self.commandline += " -explain:" + filename;
        self.commandlineArray.append("-explain:" + filename);
        return self;

    def export(self, filename):
        self.commandline += " -export:" + filename;
        self.commandlineArray.append("-export:" + filename);
        return self;

    def im(self, modename):
        self.commandline += " -im:" + modename;
        self.commandlineArray.append("-im:" + modename);
        return self;

    def it(self, template):
        self.commandline += " -it:" + template;
        self.commandlineArray.append("-it:" + template);
        return self;

    # 'on' | 'off'
    def jit(self, options):
        self.commandline += " -jit:" + options;
        self.commandlineArray.append("-jit:" + options);
        return self;

    def lib(self, filenames):
        self.commandline += " -lib:" + filenames;
        self.commandlineArray.append("-lib:" + filenames);
        return self;

    # 'on' | 'off'
    def license(self, options):
        self.commandline += " -license:" + options;
        self.commandlineArray.append("-license:" + options);
        return self;

    def m(self, classname):
        self.commandline += " -m:" + classname;
        self.commandlineArray.append("-m:" + classname);
        return self;

    def nogo(self):
        self.commandline += " -nogo";
        self.commandlineArray.append("-nogo");
        return self;

    # 'uri' | '##any' | '##html5'
    def ns(self, options):
        self.commandline += " -ns:" + options;
        self.commandlineArray.append("-ns:" + options);
        return self;

    def Or(self, classname):
        self.commandline += " -or:" + classname;
        self.commandlineArray.append("-or:" + classname);
        return self;

    # 'on' | 'off'
    def relocate(self, options):
        self.commandline += " -relocate:" + options;
        self.commandlineArray.append("-relocate:" + options);
        return self;

    # 'EE' | 'PE' | 'HE' | 'JS'
    def target(self, target):
        self.commandline += " -target:" + target;
        self.commandlineArray.append("-target:" + target);
        return self;

    def threads(self, N):
        # // todo only -S is activate
        self.commandline += " -threads:" + N;
        self.commandlineArray.append("-threads:" + N);
        return self;

    # 'silent' | 'recover' | 'fatal'
    def warnings(self, validation):
        self.commandline += " -warnings:" + validation;
        self.commandlineArray.append("-warnings:" + validation);
        return self;

    def xsl(self, filename):
        # if (!existsSync(self,filename)):
        #     throw new Error(self,'No se puede encontrar el archivo para la cadena original!.');
        # }
        self.commandline += " -xsl:" + filename
        self.commandlineArray.append("-xsl:" + filename);
        return self;

    def y(self, filename):
        self.commandline += " -y:" + filename;
        self.commandlineArray.append("-y:" + filename);
        return self;

    def params(self, value: any):
        return 1

    def getOS(self):
        if sys.platform == "Windows":
            return "transform.exe";
        elif sys.platform == 'linux':
            return 'saxon-xslt';
        elif sys.platform == 'darwin':
            return 'transform';
        return 'transform';
