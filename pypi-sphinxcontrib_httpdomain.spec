#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-sphinxcontrib_httpdomain
Version  : 1.8.0
Release  : 52
URL      : https://files.pythonhosted.org/packages/6f/00/6560676deac1d2be1009d5e14b2b16fcc9f5e9c3ac00ed50c3b297a60d3a/sphinxcontrib-httpdomain-1.8.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/6f/00/6560676deac1d2be1009d5e14b2b16fcc9f5e9c3ac00ed50c3b297a60d3a/sphinxcontrib-httpdomain-1.8.0.tar.gz
Summary  : Sphinx domain for documenting HTTP APIs
Group    : Development/Tools
License  : BSD-2-Clause
Requires: pypi-sphinxcontrib_httpdomain-license = %{version}-%{release}
Requires: pypi-sphinxcontrib_httpdomain-python = %{version}-%{release}
Requires: pypi-sphinxcontrib_httpdomain-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(six)
BuildRequires : pypi(sphinx)

%description
``sphinxcontrib.httpdomain``
============================
.. image:: https://badge.fury.io/py/sphinxcontrib-httpdomain.svg
:target: https://pypi.org/project/sphinxcontrib-httpdomain/
:alt: Latest PyPI version

%package license
Summary: license components for the pypi-sphinxcontrib_httpdomain package.
Group: Default

%description license
license components for the pypi-sphinxcontrib_httpdomain package.


%package python
Summary: python components for the pypi-sphinxcontrib_httpdomain package.
Group: Default
Requires: pypi-sphinxcontrib_httpdomain-python3 = %{version}-%{release}

%description python
python components for the pypi-sphinxcontrib_httpdomain package.


%package python3
Summary: python3 components for the pypi-sphinxcontrib_httpdomain package.
Group: Default
Requires: python3-core
Provides: pypi(sphinxcontrib_httpdomain)
Requires: pypi(six)
Requires: pypi(sphinx)

%description python3
python3 components for the pypi-sphinxcontrib_httpdomain package.


%prep
%setup -q -n sphinxcontrib-httpdomain-1.8.0
cd %{_builddir}/sphinxcontrib-httpdomain-1.8.0
pushd ..
cp -a sphinxcontrib-httpdomain-1.8.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656409326
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-sphinxcontrib_httpdomain
cp %{_builddir}/sphinxcontrib-httpdomain-1.8.0/LICENSE %{buildroot}/usr/share/package-licenses/pypi-sphinxcontrib_httpdomain/2e3d96196666de3d8582c67fcdc7804f28e1fe0c
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-sphinxcontrib_httpdomain/2e3d96196666de3d8582c67fcdc7804f28e1fe0c

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
