def validate_hello(msg):
    return any(s in msg.lower() for s in ("hello","ciao","salut","hallo","hola","ahoj","czesc"))
