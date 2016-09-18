try:
    string_type = basestr
    import StringIO
    StringIO = StringIO.StringIO
except:
    string_type = str
    import io
    StringIO = io.StringIO
