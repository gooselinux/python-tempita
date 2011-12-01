%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:           python-tempita
Version:        0.4
Release:        2%{?dist}
Summary:        A very small text templating language

Group:          Development/Languages
License:        MIT
URL:            http://pythonpaste.org/tempita/
Source0:        http://pypi.python.org/packages/source/T/Tempita/Tempita-%{version}.tar.gz
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildArch:      noarch
BuildRequires:  python-setuptools-devel
BuildRequires:  python-nose

%description
Tempita is a small templating language for text substitution.

%prep
%setup -q -n Tempita-%{version}


%build
%{__python} setup.py build


%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install --skip-build --root %{buildroot}

 
%clean
%{__rm} -rf %{buildroot}


%check
nosetests


%files
%defattr(-,root,root,-)
%doc docs/*
%{python_sitelib}/tempita
%{python_sitelib}/*.egg-info


%changelog
* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Apr 20 2009 Ricky Zhou <ricky@fedoraproject.org> - 0.4-1
- Upstream released a new version.

* Tue Apr 14 2009 Ricky Zhou <ricky@fedoraproject.org> - 0.3-3
- Change define to global.
- Remove old >= 8 conditional.
- Remove unnecessary BuildRequires on python-devel.

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Dec 06 2008 Ricky Zhou <ricky@fedoraproject.org> - 0.3-1
- Upstream released a new version.

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.0-4
- Rebuild for Python 2.6

* Mon Jul 07 2008 Ricky Zhou <ricky@fedoraproject.org> - 0.2-2
- Add %%check section.

* Sat Jun 14 2008 Ricky Zhou <ricky@fedoraproject.org> - 0.2-1
- Initial RPM Package.
