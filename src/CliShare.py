import subprocess
import sys
import os


class CliShare:
    def __int__(self):
        self.commandline = '';
        self.commandlineArray = [];
        self.saxonBin = '';
        self.commandlineArray.append(self.saxonBin)
        self.commandline = self.saxonBin;

    def catalog(self, filenames: any):
        self.commandline += " -catalog " + filenames;
        self.commandlineArray.append("-catalog " + filenames);
        return self;

    # 'on' | 'off' | 'recover'
    def dtd(self, options):
        self.commandline += " -dtd" + options;
        self.commandlineArray.append("-dtd" + options);
        return self;

    # 'on' | 'off'
    def expand(self, options):
        self.commandline += " -expand:" + options;
        self.commandlineArray.append("-expand:" + options);
        return self;

    # 'on' | 'off'
    def ext(self, options):
        self.commandline += " -ext:" + options;
        self.commandlineArray.append("-ext:" + options);
        return self;

    def init(self, initializer):
        self.commandline += " -init:" + initializer;
        self.commandlineArray.append("-init:" + initializer);
        return self;

    # 'on' | 'off'
    def l(self, options):
        self.commandline += " -l:" + options;
        self.commandlineArray.append("-l:" + options);
        return self;

    def now(self, format):
        self.commandline += " -now:" + format;
        self.commandlineArray.append("-now:" + format);
        return self;

    def o(self, filename):
        self.commandline += " -o:" + filename;
        self.commandlineArray.append("-o:" + filename);
        return self;

    # 'c' | 'd' | 'e' | 'f' | 'g' | 'j' | 'k' | 'l' | 'm' | 'n' | 'r' | 's' | 't' | 'v' | 'w' | 'x'
    def opt(self, flags):
        self.commandline += " -opt:-" + flags;
        self.commandlineArray.append("-opt:-" + flags);
        return self;

    # 'recover' | 'fatal'
    def outval(self, options):
        self.commandline += " -outval:" + options;
        self.commandlineArray.append("-outval:" + options);
        return self;

    #  'on' | 'off'
    def p(self, options):
        self.commandline += " -p:" + options;
        self.commandlineArray.append("-p:" + options);
        return self;

    # 'on' | 'off'
    def quit(self, options):
        self.commandline += " -quit:" + options;
        self.commandlineArray.append("-quit:" + options);
        return self;

    def r(self, classname):
        self.commandline += " -r:" + classname;
        self.commandlineArray.append("-r:" + classname);
        return self;

    def repeat(self, integer):
        self.commandline += " -repeat:" + integer;
        self.commandlineArray.append("-repeat:" + integer);
        return self;

    def s(self, filename):
        # if (self,!existsSync(self, filename)):
        #     throw
        #     new
        #     Error(self, 'No se puede encontrar el xml processar.');
        # }
        self.commandline += " -s:" + filename;
        self.commandlineArray.append("-s:" + filename);
        return self;

    def sa(self):
        self.commandline += " -sa";
        self.commandlineArray.append("-sa");
        return self;

    def scmin(self, filename):
        self.commandline += " -scmin:" + filename;
        self.commandlineArray.append("-scmin:" + filename);
        return self;

    # 'all' | 'none' | 'ignorable'
    def strip(self, options):
        self.commandline += " -relocate:" + options;
        self.commandlineArray.append("-relocate:" + options);
        return self;

    def t(self):
        self.commandline += " -t";
        self.commandlineArray.append("-t");
        return self;

    def T(self, classname):
        self.commandline += " -T:" + classname;
        self.commandlineArray.append("-T:" + classname);
        return self;

    def TB(self, filename):
        self.commandline += " -TB:" + filename;
        self.commandlineArray.append("-TB:" + filename);
        return self;

    def TJ(self):
        self.commandline += " -TJ";
        self.commandlineArray.append("-TJ");
        return self;

    # 'none' | 'low' | 'normal' | 'high'
    def Tlevel(self, level):
        self.commandline += " -Tlevel:" + level;
        self.commandlineArray.append("-Tlevel:" + level);
        return self;

    def Tout(self, filename):
        self.commandline += " -Tout:" + filename;
        self.commandlineArray.append("-Tout:" + filename);
        return self;

    def TP(self, filename):
        self.commandline += " -TP:" + filename;
        self.commandlineArray.append("-TP:" + filename);
        return self;

    def traceout(self, filename):
        self.commandline += " -traceout:" + filename;
        self.commandlineArray.append("-traceout:" + filename);
        return self;

    # 'linked' | 'tiny' | 'tinyc'
    def tree(self, level):
        self.commandline += " -tree:" + level;
        self.commandlineArray.append("-tree:" + level);
        return self;

    def u(self):
        self.commandline += " -u";
        self.commandlineArray.append("-u");
        return self;

    # 'strict' | 'lax'
    def val(self, validation):
        self.commandline += " -val:" + validation;
        self.commandlineArray.append("-val:" + validation);
        return self;

    def x(self, classname):
        self.commandline += " -x:" + classname;
        self.commandlineArray.append("-x:" + classname);
        return self;

    # 'on' | 'off'
    def xi(self, options):
        self.commandline += " -xi:" + options;
        self.commandlineArray.append("-xi:" + options);
        return self;

    # '1.0' | '1.1'
    def xmlversion(self, options):
        self.commandline += " -xmlversion:" + options;
        self.commandlineArray.append("-xmlversion:" + options);
        return self;

    def xsd(self, file):
        self.commandline += " -xsd:" + file;
        self.commandlineArray.append("-xsd:" + file);
        return self;

    #  '1.0' | '1.1'
    def xsdversion(self, options):
        self.commandline += " -xsdversion:" + options;
        self.commandlineArray.append("-xsdversion:" + options);
        return self;

    # 'on' | 'off'
    def xsiloc(self, options):
        self.commandline += " -xsiloc:" + options;
        self.commandlineArray.append("-xsiloc:" + options);
        return self;

    def feature(self, value):
        self.commandline += " --feature:" + value;
        self.commandlineArray.append("--feature:" + value);
        return self;

    def run(self):
        try:
            # command = os.system(self.commandline)
            # print(self.commandlineArray)
            command = subprocess.run(self.commandlineArray, stderr=False, stdout=subprocess.PIPE).stdout.decode('utf-8')
            # sys.stdout.buffer.write(command.stdout)
            # sys.stderr.buffer.write(command.stderr)
            # sys.exit(command.returncode)
            return command
        except Exception as e:
            return e
