'''
Created on May 4, 2012

@package: livedesk
@copyright: 2012 Sourcefabric o.p.s.
@license: http://www.gnu.org/licenses/gpl-3.0.txt
@author: Gabriel Nistor

Contains the SQL alchemy meta for blog post API.
'''

from ..api.blog_post import BlogPost
from sqlalchemy.schema import Column, ForeignKey
from superdesk.post.meta.post import PostMapped
from superdesk.meta.metadata_superdesk import Base
from livedesk.meta.blog import BlogMapped
from sqlalchemy.ext.declarative import declared_attr

# --------------------------------------------------------------------

#TODO: this is just a temporary extending mechanism needs to be done by using join.
class BlogPostDefinition:
    '''
    Provides the mapping for BlogCollaborator definition.
    '''
    __tablename__ = 'livedesk_post'
    __table_args__ = dict(mysql_engine='InnoDB', mysql_charset='utf8')

    Id = declared_attr(lambda cls: Column('fk_post_id', ForeignKey(PostMapped.Id), primary_key=True))
    Blog = declared_attr(lambda cls: Column('fk_blog_id', ForeignKey(BlogMapped.Id), nullable=False))

class BlogPostEntry(Base, BlogPostDefinition):
    '''
    Provides the mapping for BlogPost table where it keeps the connection between the post and the blog.
    '''
    __tablename__ = 'livedesk_post'
    __table_args__ = dict(mysql_engine='InnoDB', mysql_charset='utf8')

    Id = Column('fk_post_id', ForeignKey(PostMapped.Id), primary_key=True)
    Blog = Column('fk_blog_id', ForeignKey(BlogMapped.Id), nullable=False)

class BlogPostMapped(BlogPostDefinition, PostMapped, BlogPost):
    '''
    Provides the mapping for BlogPost in the form of extending the Post.
    '''
    __table_args__ = dict(extend_existing=True)
