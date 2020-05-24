from django.db import models


# Create your models here.

# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = data_from_dict(json.loads(json_string))

from typing import Any, TypeVar, Type, cast


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class AboutMe:
    name: str
    imagesrc: str

    def __init__(self, name: str, imagesrc: str) -> None:
        self.name = name
        self.imagesrc = imagesrc

    @staticmethod
    def from_dict(obj: Any) -> 'AboutMe':
        assert isinstance(obj, dict)
        name = from_str(obj.get("name"))
        imagesrc = from_str(obj.get("imagesrc"))
        return AboutMe(name, imagesrc)

    def to_dict(self) -> dict:
        result: dict = {}
        result["name"] = from_str(self.name)
        result["imagesrc"] = from_str(self.imagesrc)
        return result


class Home:
    title: str
    facebook_id: str
    email: str

    def __init__(self, title: str, facebook_id: str, email: str) -> None:
        self.title = title
        self.facebook_id = facebook_id
        self.email = email

    @staticmethod
    def from_dict(obj: Any) -> 'Home':
        assert isinstance(obj, dict)
        title = from_str(obj.get("title"))
        facebook_id = from_str(obj.get("facebookId"))
        email = from_str(obj.get("email"))
        return Home(title, facebook_id, email)

    def to_dict(self) -> dict:
        result: dict = {}
        result["title"] = from_str(self.title)
        result["facebookId"] = from_str(self.facebook_id)
        result["email"] = from_str(self.email)
        return result


class Data:
    home: Home
    about_me: AboutMe

    def __init__(self, home: Home, about_me: AboutMe) -> None:
        self.home = home
        self.about_me = about_me

    @staticmethod
    def from_dict(obj: Any) -> 'Data':
        assert isinstance(obj, dict)
        home = Home.from_dict(obj.get("home"))
        about_me = AboutMe.from_dict(obj.get("aboutMe"))
        return Data(home, about_me)

    def to_dict(self) -> dict:
        result: dict = {}
        result["home"] = to_class(Home, self.home)
        result["aboutMe"] = to_class(AboutMe, self.about_me)
        return result


def data_from_dict(s: Any) -> Data:
    return Data.from_dict(s)


def data_to_dict(x: Data) -> Any:
    return to_class(Data, x)

