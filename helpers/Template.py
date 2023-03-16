class Template:
    def __init__(self, nested_object, select_by, api_name, data_table):
        self.json_object_header = nested_object
        self.select_by = select_by
        self.api_name= api_name
        self.api_name_dashes = api_name.lower().replace(' ','-')
        self.api_name_noSpaces = api_name.replace(' ','') 
        self.data_table = data_table
        
