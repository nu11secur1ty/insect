#!/usr/bin/python
# Idea: Mauro Soria
# Development: nu11secur1ty - 2022

from lib.core.settings import NEW_LINE
from lib.reports.base import FileBaseReport
from lib.utils.common import escape_csv


class CSVReport(FileBaseReport):
    def get_header(self):
        return "URL,Status,Size,Content Type,Redirection" + NEW_LINE

    def generate(self, entries):
        output = self.get_header()

        for entry in entries:
            output += f"{entry.url},{entry.status},{entry.length},{entry.type},"

            if entry.redirect:
                output += f'"{escape_csv(entry.redirect)}"'

            output += NEW_LINE

        return output
