def execute(cmd):
    try:
        temp = os.popen(cmd)
        return str(temp.read())
    except Exception as e:
        print(f"发生异常{e}")
        return str(e)