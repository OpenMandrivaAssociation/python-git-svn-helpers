%define	gitdate	20091103
%define	oname	git-svn-helpers

Summary:	Command-line tools to make git-svn simple
Name:		python-%{oname}
Version:	0.6
Release:	%mkrel 0.%{gitdate}.1
License:	BSD
Group:		Development/Other
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Source0:	%{oname}-%{version}.tar.xz
URL:		http://github.com/tomster/git-svn-helpers
BuildArch:	noarch
Requires:	python-jarn.mkrelease

%description
git-svn-helpers is a collection of command line tools that greatly simplify
using git for svn repositories. It's main goal is to make setting up a local
git repository following an existing svn checkout a 'no-brainer'.
It also addresses using a single git-svn repository for working on multiple
checkouts of (usually) different branches and switching between them.

%prep
%setup -q -n %{oname}-%{version}

%build
python setup.py build

%install
rm -rf %{buildroot}
python setup.py install --root=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root, root)
%doc HISTORY.txt README.txt
%dir %{python_sitelib}/gitsvnhelpers
%{python_sitelib}/gitsvnhelpers/*.py*
%dir %{python_sitelib}/gitsvnhelpers/tests
%{python_sitelib}/gitsvnhelpers/tests/*.py*
%{python_sitelib}/gitsvnhelpers/tests/*.txt
%dir %{python_sitelib}/gitsvnhelpers/tests/testrepo.svn
%{python_sitelib}/gitsvnhelpers/tests/testrepo.svn/*
%{python_sitelib}/git_svn_helpers-%{version}-py%{python_version}.egg-info
%{_bindir}/gitify
%{_bindir}/gs-clone
%{_bindir}/gs-commit
%{_bindir}/gs-fetch

