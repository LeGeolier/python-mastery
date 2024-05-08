import stock


class TableFormatter:
    def headings(self, headers):
        raise NotImplementedError()

    def row(self, rowdata):
        raise NotImplementedError()


class TextTableFormatter(TableFormatter):
    def headings(self, headers):
        print(" ".join("%10s" % h for h in headers))
        print(("-" * 10 + " ") * len(headers))

    def row(self, rowdata):
        print(" ".join("%10s" % d for d in rowdata))


class CSVTableFormatter(TableFormatter):
    def headings(self, headers):
        print("".join("%s," % val for val in headers))

    def row(self, rowdata):
        print("".join("%s," % d for d in rowdata))


class HTMLTableFormatter(TableFormatter):
    def headings(self, headers):
        print("<tr>", end=" ")
        print(" ".join("<td>%s</td>" % val for val in headers), end=" ")
        print("</tr>")

    def row(self, rowdata):
        print("<tr>", end=" ")
        print(" ".join("<td>%s</td>" % val for val in rowdata), end=" ")
        print("</tr>")


def print_table(records, fields, formatter):
    formatter.headings(fields)
    for r in records:
        rowdata = [getattr(r, fieldname) for fieldname in fields]
        formatter.row(rowdata)


def create_formatter(name):
    if name == "html":
        return HTMLTableFormatter()
    if name == "text":
        return TextTableFormatter()
    if name == "csv":
        return CSVTableFormatter()
    raise RuntimeError("Unknown format %s" % name)
