import client


class Attachment(object):
    def __init__(self):
        self.id = None
        self.mimetype = None
        self.filename = None
        self.size = None
        self.width = None
        self.height = None
        self.url = None

    def isimage(self):
        return self.mimetype is not None and self.mimetype.startwith('image')


class Conversation(object):
    def __init__(self):
        self.id = None
        self.folderid = None
        self.isdraft = None
        self.number = None
        self.source = None
        self.owner = None
        self.mailbox = None
        self.customer = None
        self.threadcount = None
        self.status = None
        self.subject = None
        self.preview = None
        self.createdat = None
        self.modifiedat = None
        self.closedat = None
        self.closedby = None
        self.createdby = None
        self.cclist = None
        self.bcclist = None
        self.tags = None
        self._threads = None
        self._custom_fields = None

    def iscreatedbycustomer(self):
        return self.createdby is not None and isinstance(self.createdby,
                                                         CustomerRef)

    def hascclist(self):
        return self.cclist is not None and len(self.cclist) > 0

    def hasbcclist(self):
        return self.bcclist is not None and len(self.bcclist) > 0

    def hastags(self):
        return self.tags is not None and len(self.tags) > 0

    def hasthreads(self):
        return self._threads is not None and len(self._threads) > 0

    @property
    def threads(self):
        return self._threads

    @threads.setter
    def threads(self, value):
        self._threads = client.parse_list(value, "Thread")

    @property
    def customfields(self):
        return self._custom_fields

    @customfields.setter
    def customfields(self, value):
        self._custom_fields = client.parse_list(value, "Field")


class Tag(object):
    def __init__(self):
        self.id = None
        self.slug = None
        self.tag = None
        self.count = None
        self.color = None
        self.createdat = None
        self.modifiedat = None

    @property
    def name(self):
        return self.tag


class Customer(object):
    def __init__(self):
        self.id = None
        self.firstname = None
        self.lastname = None
        self.gender = None
        self.age = None
        self.joblocation = None
        self.location = None
        self.organization = None
        self.photourl = None
        self.phototype = None
        self.createdat = None
        self.modifiedat = None
        self.background = None
        self.address = None
        self.socialprofiles = None
        self.emails = None
        self.phones = None
        self.chats = None
        self.websites = None

    def hasbackground(self):
        return self.background is not None

    def hasaddress(self):
        return self.address is not None

    def hassocialprofiles(self):
        return self.socialprofiles is not None and len(self.socialprofiles) > 0

    def hasemails(self):
        return self.emails is not None

    def hasphones(self):
        return self.phones is not None and len(self.phones) > 0

    def haschats(self):
        return self.chats is not None and len(self.chats) > 0

    def haswebsites(self):
        return self.websites is not None and len(self.websites) > 0


class Folder(object):
    def __init__(self):
        self.id = None
        self.name = None
        self.type = None
        self.userid = None
        self.totalcount = None
        self.activecount = None
        self.modifiedat = None


class Mailbox(object):
    def __init__(self):
        self.id = None
        self.name = None
        self.slug = None
        self.email = None
        self.createdat = None
        self.modifiedat = None
        self._custom_fields = None

    @property
    def customfields(self):
        return self._custom_fields

    @customfields.setter
    def customfields(self, value):
        self._custom_fields = client.parse_list(value, "Field")


class Source(object):
    def __init__(self):
        self.type = None
        self.via = None

    def isviacustomer(self):
        return self.via is not None and "customer" == self.via


class User(object):
    def __init__(self):
        self.id = None
        self.firstname = None
        self.email = None
        self.role = None
        self.timezone = None
        self.photourl = None
        self.createdat = None
        self.modifiedat = None


class Address(object):
    def __init__(self):
        self.id = None
        self.lines = None
        self.city = None
        self.state = None
        self.postalcode = None
        self.country = None
        self.createdat = None
        self.modifiedat = None


class CustomerEntry(object):
    def __init__(self):
        self.id = None
        self.value = None
        self.type = None
        self.location = None


class EmailEntry(CustomerEntry):
    def __init__(self):
        super(EmailEntry, self).__init__()


class ChatEntry(CustomerEntry):
    def __init__(self):
        super(ChatEntry, self).__init__()


class PhoneEntry(CustomerEntry):
    def __init__(self):
        super(PhoneEntry, self).__init__()


class SocialProfileEntry(CustomerEntry):
    def __init__(self):
        super(SocialProfileEntry, self).__init__()


class WebsiteEntry(CustomerEntry):
    def __init__(self):
        super(WebsiteEntry, self).__init__()


class MailboxRef(object):
    def __init__(self):
        self.id = None
        self.name = None


class AbstractRef(object):
    def __init__(self):
        self.id = None
        self.firstname = None
        self.lastname = None
        self.email = None


class UserRef(AbstractRef):
    pass


class CustomerRef(AbstractRef):
    pass


class Thread(object):
    def __init__(self):
        self.id = None
        self.state = None
        self.body = None
        self.tolist = None
        self.cclist = None
        self.bcclist = None
        self.attachments = None

    def ispublished(self):
        return self.state == "published"  # hmmm these are not right

    def isdraft(self):
        return self.state == "draft"

    def isheldforreview(self):
        return self.state == "underreview"

    def hasattachments(self):
        return self.attachments is not None and len(self.attachments) > 0


class FieldOption(object):
    def __init__(self):
        self.id = None
        self.label = None
        self.order = None


class Field(object):
    def __init__(self):
        self.fieldid = None
        self.name = None
        self.value = None
        self.type = None
        self._options = None

    @property
    def options(self):
        return self._options

    @options.setter
    def options(self, value):
        self._options = client.parse_list(value, 'FieldOption')


class ForwardChild(AbstractRef):
    pass


class Note(AbstractRef):
    pass


class Message(AbstractRef):
    pass


class ForwardParent(AbstractRef):
    pass
