
### {{cookiecutter.project_name}} for Soltra Edge

__NOTE:__  Soltra Edge v2.2+ is required for the {{cookiecutter.project_name}}.  

#### License
__Soltra {{cookiecutter.project_name}}__  

*Copyright 2015 Soltra Solutions, LLC
See LICENSE.txt for more information.
STIX to Snort Rule Generator Adapter for Soltra Edge.
Please see the LICENSE.txt file for licensing details.*

*This product includes software developed at Soltra Solutions, LLC (http://www.soltra.com/).*

#### Installation
The {{cookiecutter.repo_name}} directory needs to be put into a zip-compressed tarball.  For example, the following command will generate an appropriate tarball for installation through the Edge web interface.

    tar -zcvf {{cookiecutter.repo_name}}.tgz {{cookiecutter.repo_name}}

Once you have the compressed tarball, go to the Admin -> Adapters section of your Edge installation, and follow the on-screen directions to upload and install the adapter.


#### Goals/Functionality
{{cookiecutter.short_descrioption}}

#### Process and Data Flow
At a high level, the {{cookiecutter.project_name}} is a Django App, bundled with a metadata file, INFO.json, that contains metadata about the adapter, including name, version, and compatible Edge versions.

#### MongoDB
Data is stored in MongoDB using Django Models.  With properly defined models the mongoengine backend will create your collection when specified from code.

#### Feedback
Your comments, bug reports, and pull requests are greatly appreciated!

#### TODOs
