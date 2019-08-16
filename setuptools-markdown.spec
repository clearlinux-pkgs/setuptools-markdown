#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : setuptools-markdown
Version  : 0.4.1
Release  : 4
URL      : https://files.pythonhosted.org/packages/3e/3a/b41c33a0253830bc2e2970c9437174892507eba3289f693073e8b77e1f99/setuptools-markdown-0.4.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/3e/3a/b41c33a0253830bc2e2970c9437174892507eba3289f693073e8b77e1f99/setuptools-markdown-0.4.1.tar.gz
Summary  : [Deprecated] Use Markdown for your project description
Group    : Development/Tools
License  : MIT
Requires: setuptools-markdown-license = %{version}-%{release}
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

%package license
Summary: license components for the setuptools-markdown package.
Group: Default

%description license
license components for the setuptools-markdown package.


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
%setup -q -n setuptools-markdown-0.4.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1565920255
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
mkdir -p %{buildroot}/usr/share/package-licenses/setuptools-markdown
cp LICENSE-MIT %{buildroot}/usr/share/package-licenses/setuptools-markdown/LICENSE-MIT
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/setuptools-markdown/LICENSE-MIT

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
