async def fake_stream(text):

    words = text.split()

    for word in words:

        yield word + " "