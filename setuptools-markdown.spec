#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : setuptools-markdown
Version  : 0.3
Release  : 3
URL      : https://files.pythonhosted.org/packages/b3/7f/3a0ce356e5e77dcdb56d62bf4a294d2810b06f917c87b6946103e6e17e64/setuptools-markdown-0.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/b3/7f/3a0ce356e5e77dcdb56d62bf4a294d2810b06f917c87b6946103e6e17e64/setuptools-markdown-0.3.tar.gz
Summary  : Use Markdown for your project description
Group    : Development/Tools
License  : MIT
Requires: setuptools-markdown-python = %{version}-%{release}
Requires: setuptools-markdown-python3 = %{version}-%{release}
Requires: pypandoc
BuildRequires : buildreq-distutils3
BuildRequires : pypandoc

%description
setuptools-markdown
===================
Use `Markdown <http://daringfireball.net/projects/markdown/>`__ for your
project description

%package python
Summary: python components for the setuptools-markdown package.
Group: Default
Requires: setuptools-markdown-python3 = %{version}-%{release}

%description python
python components for the setuptools-markdown package.


%package python3
Summary: python3 components for the setuptools-markdown package.
Group: Default
Requires: python3-core

%description python3
python3 components for the setuptools-markdown package.


%prep
%setup -q -n setuptools-markdown-0.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1565734095
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
