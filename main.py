#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import random

def getRandomFortune():
    #make list of possible fortunes
    fortunes = ["I see much code in your future",
    "Condsider eating more fortune cookies",
    "you have tamed the mighty python, now you must free it onto the great spiders web"]
    # randomly select a fortune
    index = random.randint(0, 2)
    return fortunes[index]

class MainHandler(webapp2.RequestHandler):
    def get(self):
        header = "<h1>Fortune Cookie</h1>"

        fortune = "<strong>" + getRandomFortune() + "</strong>"

        fortune_sentence = "Your fortune is: " + fortune
        fortune_paragraph ="<p>" + fortune_sentence + "</p>"

        lucky_number = random.randint(1, 100)
        number_sentence = 'Your lucky number is: ' + "<strong>" + str(lucky_number) + "</strong>"
        number_paragraph = "<p>" + number_sentence + "</p>"

        cookie_again = "<a href='.'><button>Another cookie, please</button> </a>"

        content = header + fortune_paragraph + number_paragraph + cookie_again

        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
