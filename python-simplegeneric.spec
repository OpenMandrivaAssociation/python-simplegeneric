%define	module	simplegeneric
%define name	python2-%{module}
%define version	0.8.1

Summary:	Simple generic Python functions
Name:		%{name}
Version:	%{version}
Release:	8
Source0:	http://pypi.python.org/packages/source/s/%{module}/%{module}-%{version}.zip
License:	ZPL
Group:		Development/Python
Url:		https://pypi.python.org/pypi/simplegeneric/
BuildArch:	noarch
BuildRequires:	python2-setuptools
%rename		python-simplegeneric

%description
The simplegeneric module lets you define simple single-dispatch
generic functions, akin to Python's built-in generic functions like
len(), iter() and so on. However, instead of using specially-named
methods, these generic functions use simple lookup tables, akin to
those used by e.g. pickle.dump() and other generic functions found in
the Python standard library.

%prep
%setup -q -n %{module}-%{version}

%build
%__python2 setup.py build

%install
PYTHONDONTWRITEBYTECODE= %__python2 setup.py install --root=%{buildroot}

%files
%defattr(-,root,root)
%doc README.txt
%py2_puresitedir/simplegeneric*


%changelog
* Wed Jun 20 2012 Lev Givon <lev@mandriva.org> 0.8.1-1
+ Revision: 806513
- imported package python-simplegeneric

