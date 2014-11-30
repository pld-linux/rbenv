Summary:	Simple per-user Ruby version manager
Name:		rbenv
Version:	0.3.0
Release:	1
License:	MIT
Group:		Development/Tools
Source0:	https://github.com/sstephenson/rbenv/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	3e2caffc7aece5e706b82bbb7dc6997b
URL:		https://github.com/sstephenson/rbenv
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir			%{_datadir}/%{name}

%description
rbenv lets you easily switch between multiple versions of Ruby. It's
simple, unobtrusive, and follows the UNIX tradition of single-purpose
tools that do one thing well.

%package -n bash-completion-%{name}
Summary:	bash completion for rbenv
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	bash-completion

%description -n bash-completion-%{name}
This package provides bash completion scripts for rbenv

%package zsh
Summary:	zsh completion for rbenv
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	zsh

%description zsh
This package provides zsh completion scripts for rbenv

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}
install -p libexec/* $RPM_BUILD_ROOT%{_datadir}/%{name}

install -d $RPM_BUILD_ROOT%{_bindir}
ln -s %{_datadir}/%{name}/rbenv $RPM_BUILD_ROOT%{_bindir}/rbenv
install -p bin/ruby-local-exec $RPM_BUILD_ROOT%{_bindir}/ruby-local-exec

install -d $RPM_BUILD_ROOT{/etc/bash_completion.d,%{_datadir}/zsh/site-functions}
install -p completions/rbenv.bash $RPM_BUILD_ROOT/etc/bash_completion.d/rbenv
install -p completions/rbenv.zsh $RPM_BUILD_ROOT%{_datadir}/zsh/site-functions/rbenv

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
%attr(755,root,root) %{_bindir}/ruby-local-exec
%dir %{_datadir}/%{name}
%attr(755,root,root) %{_datadir}/%{name}/rbenv*

%files -n bash-completion-%{name}
%defattr(644,root,root,755)
/etc/bash_completion.d/rbenv

%files zsh
%defattr(644,root,root,755)
%{_datadir}/zsh/site-functions/rbenv
