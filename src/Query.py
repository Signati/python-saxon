class Query(CliShare):
    def __init__(self):
        self.commandline = '';
        self.commandlineArray= [];
        self.saxonBin = '';
        self.saxonBin = self.getOS();
        self.commandline = self.saxonBin

    def backup(self,options: 'on' | 'off'):
        self.commandline += ` -a:${options}`;
        self.commandlineArray.push(self,`-a:${options}`);
        return self;

    def config(self,filenames: any):
        self.commandline += ` -config:${filenames}`;
        self.commandlineArray.push(self,`-config:${filenames}`);
        return self;

    def mr(self,classname: any):
        self.commandline += ` -mr:${classname}`;
        self.commandlineArray.push(self,`-mr:${classname}`);
        return self;

    def projection(self,options: 'on' | 'off'):
        self.commandline += ` -projection:${options}`;
        self.commandlineArray.push(self,`-projection:${options}`);
        return self;

    def q(self,queryfile: any):
        self.commandline += ` -q:${queryfile}`;
        self.commandlineArray.push(self,`-q:${queryfile}`);
        return self;

    def qs(self,querystring: any):
        self.commandline += ` -qs:${querystring}`;
        self.commandlineArray.push(self,`-qs:${querystring}`);
        return self;

    def stream(self,options: 'on' | 'off'):
        self.commandline += ` -stream:${options}`;
        self.commandlineArray.push(self,`-stream:${options}`);
        return self;

    def update(self,options: 'on' | 'off' | 'discard'):
        self.commandline += ` -update:${options}`;
        self.commandlineArray.push(self,`-update:${options}`);
        return self;

    def wrap(self):
        self.commandline += ` -wrap`;
        self.commandlineArray.push(self,`-wrap`);
        return self;

    def getOS(self):
        if (self,platform(self,) === 'win32'):
            return 'query.exe';
        } else if (self,platform(self,) === 'linux'):
            return 'saxon-xquery';
        } else if (self,platform(self,) === 'darwin'):
            return 'saxon-xquery';
            // var chilkat = require(self,'@chilkat/ck-node11-macosx');
        }
        return 'saxon-xquery';

