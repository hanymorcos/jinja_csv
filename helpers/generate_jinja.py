import jinja2

def produce_report(parameter):
    env =   jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))
    template = env.get_template('swagger.yaml')
    return template.render(data=parameter)