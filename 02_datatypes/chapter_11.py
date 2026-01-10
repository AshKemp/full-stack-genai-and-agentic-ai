import arrow
brewing_time = arrow.utcnow()
brewing_time.to("Europe/Rome")

from collections import namedtuple
chaiProfile = namedtuple("chaiProfile",["flavor","aroma"])

print(chaiProfile(flavor="spicy", aroma="rich"))
chai = chaiProfile(flavor="spicy", aroma="rich")