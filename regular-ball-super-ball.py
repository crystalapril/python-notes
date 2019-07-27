'''
tag:
class,property
'''

#answer1.0 by april
class Ball:
    def __init__(self,*ball_type):
        if bool(ball_type) == False:
            self.ball_type = "regular"
        else:
            self.ball_type = ball_type[0]
            
#answer2.0
class Ball(object):
  def __init__(self, type = "regular"):
    self.ball_type = type
    
#answer3.0
class Ball(object):
    def __init__(self, ball_type=None):
        self.ball_type = ball_type or "regular"
        
#answer4.0
class Ball(str): 
    ball_type = property(lambda s: s or 'regular')
    
#answer5.0
class Ball(object):

    ball_type = 'regular'
    
    def __init__(self, *kwargs):
        if kwargs:
            if kwargs[0] == 'super':
                self.ball_type = kwargs[0]
