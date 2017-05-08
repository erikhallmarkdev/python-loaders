import sys

def indeterminate_progressbar(status = ""):
    indeterminate_progressbar.current += 1;
    bar_length = 60;

    i = indeterminate_progressbar.current % bar_length

    start = i
    end = bar_length - i - 1

    bar = "[" + "." * start + " " * end + "]" + status  + "\r"

    sys.stdout.write(bar)
    sys.stdout.flush()


indeterminate_progressbar.current = 0;
