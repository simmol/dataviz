# Import application
from run import app

#Import cherrypy
import cherrypy

if __name__ == '__main__':
    
    # Mount the application
    cherrypy.tree.graft(app, "/")

    # unsubscribe default server
    cherrypy.server.unsubscribe()

    server = cherrypy._cpserver.Server()
            
    server.socket_host = "0.0.0.0"
    server.socket_port = 80
    server.thread_pool = 30

    server.subscribe()

    cherrypy.engine.start()
    cherrypy.engine.block()

               
