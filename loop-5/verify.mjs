#!/usr/bin/env node
import {readFile,readdir} from 'node:fs/promises';
import {resolve as pathResolve} from 'node:path';
import {webcrypto} from 'node:crypto';
import {loadRelease,acceptance} from './consumer.mjs';
globalThis.crypto??=webcrypto;
const root=pathResolve(process.argv[2]||'.'),expectedManifestHash=process.argv[3]||null;
async function list(dir='',out=[]) {for(const x of await readdir(pathResolve(root,dir),{withFileTypes:true})){const p=dir?dir+'/'+x.name:x.name;if(x.isSymbolicLink())throw Error('Symlinks are not release artifacts');if(x.isDirectory())await list(p,out);else out.push(p);}return out;}
try {
  const loaded=await loadRelease(p=>readFile(pathResolve(root,p)),{expectedManifestHash,listPaths:()=>list()});
  console.log(JSON.stringify({manifest_hash:loaded.manifestHash,validation:loaded.validation,clean_load:acceptance(loaded.files)},null,2));
}catch(e){console.error(e.stack);process.exitCode=1;}
