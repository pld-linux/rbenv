Summary:	Simple per-user Ruby version manager
Name:		rbenv
Version:	0.4.0
Release:	1
License:	MIT
Group:		Development/Tools
Source0:	https://github.com/sstephenson/rbenv/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	c4a15a4dccf3dc1d28d08e87fb7c7789
URL:		https://github.com/sstephenson/rbenv
Requires:	bash
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir			%{_datadir}/%{name}

%description
rbenv lets you easily switch between multiple versions of Ruby. It's
simple, unobtrusive, and follows the UNIX tradition of single-purpose
tools that do one thing well.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -a bin libexec completions $RPM_BUILD_ROOT%{_datadir}/%{name}

install -d $RPM_BUILD_ROOT%{_bindir}
ln -s %{_datadir}/%{name}/bin/%{name} $RPM_BUILD_ROOT%{_bindir}/rbenv

%post
%banner %{name} -e -o <<'EOF'
You probably want to execute the following line to add rbenv to your shell:

echo 'eval "$(rbenv init -)"' >> ~/.bash_profile
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md LICENSE
%attr(755,root,root) %{_bindir}/rbenv
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/bin
%attr(755,root,root) %{_datadir}/%{name}/bin/rbenv
%attr(755,root,root) %{_datadir}/%{name}/bin/ruby-local-exec
%dir %{_datadir}/%{name}/libexec
%attr(755,root,root) %{_datadir}/%{name}/libexec/rbenv*
%{_datadir}/%{name}/completions
