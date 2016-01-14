%global pkg_name maven-clean-plugin
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

Name:           %{?scl_prefix}%{pkg_name}
Version:        2.5
Release:        8.9%{?dist}
Summary:        Maven Clean Plugin

License:        ASL 2.0
URL:            http://maven.apache.org/plugins/maven-clean-plugin/
Source0:        http://repo1.maven.org/maven2/org/apache/maven/plugins/%{pkg_name}/%{version}/%{pkg_name}-%{version}-source-release.zip

BuildArch: noarch

BuildRequires:  %{?scl_prefix_java_common}maven-local
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven.plugins:maven-plugins:pom:)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  %{?scl_prefix}mvn(org.codehaus.plexus:plexus-utils)


%description
The Maven Clean Plugin is a plugin that removes files generated 
at build-time in a project's directory.

%package javadoc
Summary:        Javadoc for %{pkg_name}

%description javadoc
API documentation for %{pkg_name}.


%prep
%setup -q -n %{pkg_name}-%{version}
%{?scl:scl enable %{scl_java_common} %{scl_maven} %{scl} - <<"EOF"}
set -e -x
# maven-core has scope "provided" in Plugin Testing Harness, so we
# need to provide it or tests will fail to compile.  This works for
# upstream because upstream uses a different version of Plugin Testing
# Harness in which scope of maven-core dependency is "compile".
%pom_add_dep org.apache.maven:maven-core::test
%{?scl:EOF}

%build
%{?scl:scl enable %{scl_java_common} %{scl_maven} %{scl} - <<"EOF"}
set -e -x
%mvn_build -f
%{?scl:EOF}

%install
%{?scl:scl enable %{scl_java_common} %{scl_maven} %{scl} - <<"EOF"}
set -e -x
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%dir %{_mavenpomdir}/%{pkg_name}
%dir %{_javadir}/%{pkg_name}
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Thu Jan 15 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.5-8.9
- Add directory ownership on %%{_mavenpomdir} subdir

* Wed Jan 14 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.5-8.8
- Fix BR on maven-plugins parent POM

* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 2.5-8.8
- Mass rebuild 2015-01-13

* Tue Jan 06 2015 Michael Simacek <msimacek@redhat.com> - 2.5-8.7
- Mass rebuild 2015-01-06

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.5-8.6
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.5-8.5
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.5-8.4
- Mass rebuild 2014-02-18

* Fri Feb 14 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.5-8.3
- SCL-ize requires and build-requires

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.5-8.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.5-8.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 2.5-8
- Mass rebuild 2013-12-27

* Thu Aug 22 2013 Michal Srb <msrb@redhat.com> - 2.5-7
- Migrate away from mvn-rpmbuild (Resolves: rhbz#997470)

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.5-6
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Mon Mar 11 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.5-5
- Add maven-core to test dependencies
- Resolves: rhbz#914165

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 2.5-3
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jun 17 2012 Alexander Kurtakov <akurtako@redhat.com> 2.5-1
- Update to new upstream version.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jun 8 2011 Alexander Kurtakov <akurtako@redhat.com> 2.4.1-4
- Build with maven 3.x.
- Use upstream sources.
- Guidelines fixes.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed May 12 2010 Alexander Kurtakov <akurtako@redhat.com> 2.4.1-2
- Fix review comments.

* Wed May 12 2010 Alexander Kurtakov <akurtako@redhat.com> 2.4.1-1
- Initial package.
