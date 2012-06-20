%define	module	simplegeneric
%define name	python-%{module}
%define version	0.8.1
%define rel		1
%if %mdkversion < 201100
%define release	%mkrel %{rel}
%else
%define release %{rel}
%endif

Summary:	Simple generic Python functions
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://pypi.python.org/packages/source/s/%{module}/%{module}-%{version}.zip
License:	ZPL
Group:		Development/Python
Url:		http://pypi.python.org/pypi/simplegeneric/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
BuildRequires:	python-setuptools

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
%__python setup.py build

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README.txt
%py_sitedir/simplegeneric*
