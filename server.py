import tornado.ioloop
import tornado.web
import json


settings = {
	"static_path": 'static',
	"template_path": 'template',
	"debug" : True

}


class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.render('resume.html')

class Research_list(tornado.web.RequestHandler):
	def get(self):
		json_data = open('research')
		data = json.load(json_data)
		for i in data:
			html_adress_for_article = self.reverse_url("article", i['title'])
			i['html_address'] = html_adress_for_article
		self.render('research_list.html', data = data)

class Research_article(tornado.web.RequestHandler):
	def get(self, article_name):
		# json_data = open('research')
		# data = json.load(json_data)
		self.render('content/research/' + article_name + '/article.html')

if __name__ == "__main__":
	name = "article"
	application = tornado.web.Application([
		(r"/", MainHandler),
		(r"/app_static/(.*)", tornado.web.StaticFileHandler, {"path": "template"}),
		tornado.web.URLSpec(r"/research/(.*)", Research_article, name = "article"),
		(r"/research", Research_list)
	], **settings)
	application.listen(80)
	tornado.ioloop.IOLoop.current().start()