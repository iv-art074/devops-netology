#N1 
$ git show aefea   
commit aefead2207ef7e2aa5dc81a34aedf0cad4c32545   
Author: Alisdair McDiarmid <alisdair@users.noreply.github.com>   
Date:   Thu Jun 18 10:29:58 2020 -0400   
   
    Update CHANGELOG.md   

#N2
$ git log 85024d3 --oneline  
85024d310 (tag: v0.12.23) v0.12.23

#N3
iv_ar@Pappa MINGW64 ~/documents/github/devops-netology/tools/terraform (main)  
$ git log --oneline --no-walk b8d720^@  
9ea88f22f add/update community provider listings  
56cd7859e Merge pull request #23857 from hashicorp/cgriggs01-stable  

#N4
$ git checkout v0.12.23  
Updating files: 100% (9255/9255), done.  
Note: switching to 'v0.12.23'.  

You are in 'detached HEAD' state. You can look around, make experimental  
changes and commit them, and you can discard any commits you make in this   
state without impacting any branches by switching back to a branch.  

If you want to create a new branch to retain commits you create, you may  
do so (now or later) by using -c with the switch command. Example:  

  git switch -c <new-branch-name>                                    

Or undo this operation with:

  git switch -

Turn off this advice by setting config variable advice.detachedHead to false

HEAD is now at 85024d310 v0.12.23

$ git checkout v0.12.24  
Previous HEAD position was 85024d310 v0.12.23  
HEAD is now at 33ff1c03b v0.12.24  

$ git log 85024..33ff1 --oneline  
33ff1c03b (HEAD, tag: v0.12.24) v0.12.24  
b14b74c49 [Website] vmc provider links  
3f235065b Update CHANGELOG.md  
6ae64e247 registry: Fix panic when server is unreachable  
5c619ca1b website: Remove links to the getting started guide's old location  
06275647e Update CHANGELOG.md  
d5f9411f5 command: Fix bug when using terraform login on Windows  
4b6d06cc5 Update CHANGELOG.md  
dd01a3507 Update CHANGELOG.md  
225466bc3 Cleanup after v0.12.23 release  

#N5  

 git grep 'providerSource'  


	provider_source.go:// providerSource constructs a provider source based on a combination of the  
	provider_source.go:func providerSource(configs []*cliconfig.ProviderInstallation, services *disco.Disco) (getproviders.Source, tfdiags.Diagnostics) {  
 git log -L :providerSource:provider_source.go  
	commit 8c928e83589d90a031f811fae52a81be7153e82f
	Author: Martin Atkins <mart@degeneration.co.uk>
	Date:   Thu Apr 2 18:04:39 2020 -0700

#N6

$ git grep "globalPluginDirs"  
commands.go:            GlobalPluginDirs: globalPluginDirs(),  
commands.go:    helperPlugins := pluginDiscovery.FindPlugins("credentials", globalPluginDirs())  
internal/command/cliconfig/config_unix.go:              // FIXME: homeDir gets called from globalPluginDirs during init, before  
plugins.go:// globalPluginDirs returns directories that should be searched for  
plugins.go:func globalPluginDirs() []string {  

$ git log -L :globalPluginDirs:plugins.go  
*spisok*

#N7
iv_ar@Pappa MINGW64 ~/documents/github/devops-netology/tools/terraform (main)  
$ git log -S "synchronizedWriters" --oneline --pretty="%H author %an"   
bdfea50cc85161dea41be0fe3381fd98731ff786 author James Bardin   
fd4f7eb0b935e5a838810564fd549afe710ae19a author James Bardin   
5ac311e2a91e381e2f52234668b49ba670aa0fe5 author Martin Atkins   



