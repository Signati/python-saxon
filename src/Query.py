from CliShare import CliShare
import sys


class Query(CliShare):
    def __init__(self):
        self.commandline = '';
        self.commandlineArray = [];
        self.saxonBin = '';
        self.saxonBin = self.getOS();
        self.commandline = self.saxonBin

    # 'on' | 'off'
    def backup(self, options):
        self.commandline += " -a:" + options;
        self.commandlineArray.append("-a:" + options);
        return self;

    def config(self, filenames):
        self.commandline += " -config:" + filenames;
        self.commandlineArray.append("-config:" + filenames);
        return self;

    def mr(self, classname):
        self.commandline += " -mr:" + classname;
        self.commandlineArray.append("-mr:" + classname);
        return self;

    #  'on' | 'off'
    def projection(self, options):
        self.commandline += " -projection:" + options;
        self.commandlineArray.append("-projection:" + options);
        return self;

    def q(self, queryfile):
        self.commandline += " -q:" + queryfile;
        self.commandlineArray.append("-q:" + queryfile);
        return self;

    def qs(self, querystring):
        self.commandline += " -qs:" + querystring;
        self.commandlineArray.append("-qs:" + querystring);
        return self;

    # 'on' | 'off'
    def stream(self, options):
        self.commandline += " -stream:" + options;
        self.commandlineArray.append("-stream:" + options);
        return self;

    # 'on' | 'off' | 'discard'
    def update(self, options):
        self.commandline += " -update:" + options;
        self.commandlineArray.append("-update:" + options);
        return self;

    def wrap(self):
        self.commandline += " -wrap";
        self.commandlineArray.append("-wrap");
        return self;

    def getOS(self):
        if sys.platform == "Windows":
            return "transform.exe";
        elif sys.platform == 'linux':
            return 'saxon-xslt';
        elif sys.platform == 'darwin':
            return 'transform';
        return 'transform';
