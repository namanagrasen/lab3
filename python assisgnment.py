class Shape:
    name = "Shape"

    def __str__( self ):
        return "I am a " + self.name + " defined as " + type( self ).__name__ + "( ... )"

class Square( Shape ):
    name = "Square"

    x = 0

    def __init__( self, _x ):
        super( ).__init__( )
        self.x = _x

    def __str__( self ):
        return "I am a " + self.name + " defined as " + type( self ).__name__ + "( " + str( self.x ) + " ) ie x = " + str( self.x ) + " with an area of " + str( self.area( ) )

    def area( self ):
        return self.x * self.x

class Cube( Square ):
    name = "Cube"

    def __init__( self, _x ):
        super( ).__init__( _x )

    def __str__( self ):
        return super( ).__str__( ) + " with an area of " + str( self.area( ) )

    def area( self ):
        return self.x ** self.x

class Rect( Square ):
    name = "Rectangle"
    y = 0

    def __init__( self, _x, _y ):
        super( ).__init__( _x )
        self.y = _y

    def __str__( self ):
        return "I am a " + self.name + " defined as " + type( self ).__name__ + "( " + str( self.x ) + ", " + str( self.y ) + " ) ie x = " + str( self.x ) + " / y = " + str( self.y ) + " with an area of " + str( self.area( ) )

    def area( self ):
        return self.x * self.y

def main( ):
    _shape = Rect( 10, 20 )

    _shape2 = Rect( 30, 40 )

    _shape3 = Square( 50 )

    _shape4 = Shape( )

    _shape5 = Cube( 4 )

    _text = ""

   
    _text += str( _shape ) + "\n"

    
    _text += str( super( Rect, _shape ).__str__( ) ) + "\n"

    
    _text += str( super( Square, _shape ).__str__( ) ) + "\n"

    
    _text += str( _shape2 ) + "\n"

   
    _text += str( _shape3 ) + "\n"

    
    _text += str( _shape4 ) + "\n"

   
    _text += str( _shape5 ) + "\n"

   
    return _text

print( main( ) )



