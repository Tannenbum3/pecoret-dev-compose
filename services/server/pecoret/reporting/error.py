class ReportError:
    """Define a report error.
    report errors can be created if a specific part is not completed but required in the report.
    """

    def __init__(self, message, url, edit_link=None):
        self.message = message
        self.url = url
        self.edit_link = edit_link
