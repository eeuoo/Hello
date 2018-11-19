class Game:

    def __init__(self, tag):
        self.title = self.get_text(tag, 'a.title')
        self.comp = self.get_attr(tag, 'a.subtitle', 'title')
                             
    def get_text(self, parent_tag, selector):
       tag = self.get_tag(parent_tag, selector)
       return tag.text.strip()
        
    def get_attr(self, parent_tag, selector, attr_name):
        tag = self.get_tag(parent_tag, selector)
        return tag.text.strip()
        

    def get_tag(self, tag, parent_tag, selector):
        return parent_tag.select(selector)[0]
        # return '' if t == none else t.text.strip
        if tag == None or len(tag) == 0:
            return None
        else:
            return tag[0]

    def __str__(self):
        return self.to_str()

    def to_str(self):
        return("{}\t{}".format(self.title, self.comp))           