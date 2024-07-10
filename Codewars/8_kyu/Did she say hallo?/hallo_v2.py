def validate_hello(msg):
    return any(map(msg.lower().__contains__, ("hello","ciao","salut","hallo","hola","ahoj","czesc")))
