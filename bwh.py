# -*- coding: utf-8 -*-
"""
description:
    This is a simple bwhosting api operation encapsulation

@author: wicos
@email:wicos@wicos.cn
"""

import requests as rq
import json
import math as mt

class Bwh:
    def __init__(self,veid,apikey):
        self.veid = str(veid)
        self.apikey = str(apikey)
        url = 'https://api.64clouds.com/v1/getServiceInfo?veid='+self.veid+'&api_key='+self.apikey
        try:
            getMsg = rq.get(url)
            getJson = json.loads(getMsg.text.replace("'",'"'))
            self.ip = getJson['ip_addresses'][0]
            self.os = getJson['os']
            self.email = getJson['email']
            self.hostname = getJson['hostname']
            self.nodeIp = getJson['node_ip']
            self.nodeLocation = getJson['node_location']
            self.nodeLocationId = getJson['node_location_id']
            self.nodeDatacenter = getJson['node_datacenter']
            self.disk = getJson['plan_disk']/mt.pow(1024,3)
            self.ram = getJson['plan_ram']/mt.pow(1024,3)
            self.swap = getJson['plan_swap']/mt.pow(1024,3)
        except:
            failed = json.loads('{"status":"error","name":"'+str(self.__init__.__name__)+'"}')
            return failed
    
    def getServiceInfo(self):
        url = 'https://api.64clouds.com/v1/getServiceInfo?veid='+self.veid+'&api_key='+self.apikey
        try:
            getMsg = rq.get(url)
            getJson = json.loads(getMsg.text.replace("'",'"'))
            return getJson
        except:
            failed = json.loads('{"status":"error","name":"'+str(self.getServiceInfo.__name__)+'"}')
            return failed
    
    def creatSnapshots(self,description):
        url = 'https://api.64clouds.com/v1/snapshot/create?description='+description+'&veid='+self.veid+'&api_key='+self.apikey
        try:
            getMsg = rq.get(url)
            getJson = json.loads(getMsg.text.replace("'",'"'))
            return getJson
        except:
            failed = json.loads('{"status":"error","name":"'+str(self.creatSnapshots.__name__)+'"}')
            return failed
    
    def restart(self):
        url = 'https://api.64clouds.com/v1/restart?veid='+self.veid+'&api_key='+self.apikey
        try:
            getMsg = rq.get(url)
            getJson = json.loads(getMsg.text.replace("'",'"'))
            return getJson
        except:
            failed = json.loads('{"status":"error","name":"'+str(self.restart.__name__)+'"}')
            return failed
  
    def setPtrRecord(self,ip,ptr):
        url = 'https://api.64clouds.com/v1/setPTR?ip='+str(ip)+'&ptr='+str(ptr)+'&veid='+self.veid+'&api_key='+self.apikey
        try:
            getMsg = rq.get(url)
            getJson = json.loads(getMsg.text.replace("'",'"'))
            return getJson
        except:
            failed = json.loads('{"status":"error","name":"'+str(self.setPtrRecord.__name__)+'"}')
            return failed
            
    def stop(self):
        url = 'https://api.64clouds.com/v1/stop?veid='+self.veid+'&api_key='+self.apikey
        try:
            getMsg = rq.get(url)
            getJson = json.loads(getMsg.text.replace("'",'"'))
            return getJson
        except:
            failed = json.loads('{"status":"error","name":"'+str(self.stop.__name__)+'"}')
            return failed
            
    def start(self):
        url = 'https://api.64clouds.com/v1/start?veid='+self.veid+'&api_key='+self.apikey
        try:
            getMsg = rq.get(url)
            getJson = json.loads(getMsg.text.replace("'",'"'))
            return getJson
        except:
            failed = json.loads('{"status":"error","name":"'+str(self.start.__name__)+'"}')
            return failed
            
    def kill(self):
        url = 'https://api.64clouds.com/v1/kill?veid='+self.veid+'&api_key='+self.apikey
        try:
            getMsg = rq.get(url)
            getJson = json.loads(getMsg.text.replace("'",'"'))
            return getJson
        except:
            failed = json.loads('{"status":"error","name":"'+str(self.kill.__name__)+'"}')
            return failed
            
    def getAvailableOS(self):
        url = 'https://api.64clouds.com/v1/getAvailableOS?veid='+self.veid+'&api_key='+self.apikey
        try:
            getMsg = rq.get(url)
            getJson = json.loads(getMsg.text.replace("'",'"'))
            return getJson
        except:
            failed = json.loads('{"status":"error","name":"'+str(self.getAvailableOS.__name__)+'"}')
            return failed
            
    def reinstallOS(self,osName):
        getOs = self.getAvailableOS(self)
        if getOs != 'GetAvailableOS failed,Please try again.':
            if osName in getOs['templates']:
                url = 'https://api.64clouds.com/v1/reinstallOS?os='+osName+'&veid='+self.veid+'&api_key='+self.apikey
            else:
                failed = json.loads('{"status":"error","name":"'+str(self.reinstallOS.__name__)+'"}')
                return failed
        try:
            getMsg = rq.get(url)
            getJson = json.loads(getMsg.text.replace("'",'"'))
            return getJson
        except:
            failed = json.loads('{"status":"error","name":"'+str(self.reinstallOS.__name__)+'"}')
            return failed
            
    def resetRootPassword(self):
        url = 'https://api.64clouds.com/v1/resetRootPassword?veid='+self.veid+'&api_key='+self.apikey
        try:
            getMsg = rq.get(url)
            getJson = json.loads(getMsg.text.replace("'",'"'))
            return getJson
        except:
            failed = json.loads('{"status":"error","name":"'+str(self.resetRootPassword.__name__)+'"}')
            return failed
            
    def getUsageGraphs(self):
        url = 'https://api.64clouds.com/v1/getUsageGraphs?veid='+self.veid+'&api_key='+self.apikey
        try:
            getMsg = rq.get(url)
            getJson = json.loads(getMsg.text.replace("'",'"'))
            return getJson
        except:
            failed = json.loads('{"status":"error","name":"'+str(self.getUsageGraphs.__name__)+'"}')
            return failed
        
    def getRawUsageStats(self):
        url = 'https://api.64clouds.com/v1/getRawUsageStats?veid='+self.veid+'&api_key='+self.apikey
        try:
            getMsg = rq.get(url)
            getJson = json.loads(getMsg.text.replace("'",'"'))
            return getJson
        except:
            failed = json.loads('{"status":"error","name":"'+str(self.getRawUsageStats.__name__)+'"}')
            return failed
        
    def getAuditLog(self):
        url = 'https://api.64clouds.com/v1/getAuditLog?veid='+self.veid+'&api_key='+self.apikey
        try:
            getMsg = rq.get(url)
            getJson = json.loads(getMsg.text.replace("'",'"'))
            return getJson
        except:
            failed = json.loads('{"status":"error","name":"'+str(self.getAuditLog.__name__)+'"}')
            return failed
        
    def setHostname(self,newHostname):
        url = 'https://api.64clouds.com/v1/getRawUsageStats?newHostname='+newHostname+'&veid='+self.veid+'&api_key='+self.apikey
        try:
            getMsg = rq.get(url)
            getJson = json.loads(getMsg.text.replace("'",'"'))
            return getJson
        except:
            failed = json.loads('{"status":"error","name":"'+str(self.setHostname.__name__)+'"}')
            return failed
        
    def getSnapshotList(self):
        url = 'https://api.64clouds.com/v1/snapshot/list?veid='+self.veid+'&api_key='+self.apikey
        try:
            getMsg = rq.get(url)
            getJson = json.loads(getMsg.text.replace("'",'"'))
            return getJson
        except:
            failed = json.loads('{"status":"error","name":"'+str(self.getSnapshotList.__name__)+'"}')
            return failed
        
    def snapshotDelete	(self,snapshot):
        url = 'https://api.64clouds.com/v1/snapshot/delete?snapshot='+snapshot+'&veid='+self.veid+'&api_key='+self.apikey
        try:
            getMsg = rq.get(url)
            getJson = json.loads(getMsg.text.replace("'",'"'))
            return getJson
        except:
            failed = json.loads('{"status":"error","name":"'+str(self.snapshotDelete.__name__)+'"}')
            return failed
        
    def snapshotRestore(self,snapshot):
        url = 'https://api.64clouds.com/v1/snapshot/restore?snapshot='+snapshot+'&veid='+self.veid+'&api_key='+self.apikey
        try:
            getMsg = rq.get(url)
            getJson = json.loads(getMsg.text.replace("'",'"'))
            return getJson
        except:
            failed = json.loads('{"status":"error","name":"'+str(self.snapshotRestore.__name__)+'"}')
            return failed
        
    def snapshotToggleSticky(self,snapshot,sticky):
        a = [1,0]
        if sticky in a:
            url = 'https://api.64clouds.com/v1/snapshot/toggleSticky?snapshot='+snapshot+'&sticky='+int(sticky)+'&veid='+self.veid+'&api_key='+self.apikey
        else:
            failed = json.loads('{"status":"error","name":"'+str(self.snapshotToggleSticky.__name__)+'","oth":"Please input sticky, 1 to set sticky attribute, 0 to remove sticky attribute."}')
            return failed
        try:
            getMsg = rq.get(url)
            getJson = json.loads(getMsg.text.replace("'",'"'))
            return getJson
        except:
            failed = json.loads('{"status":"error","name":"'+str(self.snapshotToggleSticky.__name__)+'"}')
            return failed
        
    def snapshotExport(self,snapshot):
        url = 'https://api.64clouds.com/v1/snapshot/export?snapshot='+snapshot+'&veid='+self.veid+'&api_key='+self.apikey
        try:
            getMsg = rq.get(url)
            getJson = json.loads(getMsg.text.replace("'",'"'))
            return getJson
        except:
            failed = json.loads('{"status":"error","name":"'+str(self.snapshotExport.__name__)+'"}')
            return failed
        
    def snapshotImport(self,sourceVeid,sourceToken):
        url = 'https://api.64clouds.com/v1/snapshot/import?sourceVeid='+sourceVeid+'&sourceToken='+sourceToken+'&veid='+self.veid+'&api_key='+self.apikey
        try:
            getMsg = rq.get(url)
            getJson = json.loads(getMsg.text.replace("'",'"'))
            return getJson
        except:
            failed = json.loads('{"status":"error","name":"'+str(self.snapshotImport.__name__)+'"}')
            return failed
        
    def getBackupList(self):
        url = 'https://api.64clouds.com/v1/backup/list?veid='+self.veid+'&api_key='+self.apikey
        try:
            getMsg = rq.get(url)
            getJson = json.loads(getMsg.text.replace("'",'"'))
            return getJson
        except:
            failed = json.loads('{"status":"error","name":"'+str(self.getBackupList.__name__)+'"}')
            return failed
        
    def backupCopyToSnapshot(self,backup_token):
        url = 'https://api.64clouds.com/v1/backup/copyToSnapshot?backup_token='+backup_token+'&veid='+self.veid+'&api_key='+self.apikey
        try:
            getMsg = rq.get(url)
            getJson = json.loads(getMsg.text.replace("'",'"'))
            return getJson
        except:
            failed = json.loads('{"status":"error","name":"'+str(self.backupCopyToSnapshot.__name__)+'"}')
            return failed
        
    def ipv6Add(self,ip):
        url = 'https://api.64clouds.com/v1/ipv6/add?ip='+str(ip)+'&veid='+self.veid+'&api_key='+self.apikey
        try:
            getMsg = rq.get(url)
            getJson = json.loads(getMsg.text.replace("'",'"'))
            return getJson
        except:
            failed = json.loads('{"status":"error","name":"'+str(self.ipv6Add.__name__)+'"}')
            return failed
        
    def ipv6Delete(self,ip):
        url = 'https://api.64clouds.com/v1/ipv6/delete?ip='+str(ip)+'&veid='+self.veid+'&api_key='+self.apikey
        try:
            getMsg = rq.get(url)
            getJson = json.loads(getMsg.text.replace("'",'"'))
            return getJson
        except:
            failed = json.loads('{"status":"error","name":"'+str(self.ipv6Delete.__name__)+'"}')
            return failed
        
    def migrateGetLocations(self):
        url = 'https://api.64clouds.com/v1/migrate/getLocations?veid='+self.veid+'&api_key='+self.apikey
        try:
            getMsg = rq.get(url)
            getJson = json.loads(getMsg.text.replace("'",'"'))
            return getJson
        except:
            failed = json.loads('{"status":"error","name":"'+str(self.migrateGetLocations.__name__)+'"}')
            return failed
        
    def migrateStart(self,location):
        url = 'https://api.64clouds.com/v1/migrate/start?location='+location+'&veid='+self.veid+'&api_key='+self.apikey
        try:
            getMsg = rq.get(url)
            getJson = json.loads(getMsg.text.replace("'",'"'))
            return getJson
        except:
            failed = json.loads('{"status":"error","name":"'+str(self.migrateStart.__name__)+'"}')
            return failed
        
    def getSuspensionDetails(self):
        url = 'https://api.64clouds.com/v1/getSuspensionDetails?veid='+self.veid+'&api_key='+self.apikey
        try:
            getMsg = rq.get(url)
            getJson = json.loads(getMsg.text.replace("'",'"'))
            return getJson
        except:
            failed = json.loads('{"status":"error","name":"'+str(self.getSuspensionDetails.__name__)+'"}')
            return failed
        
    def getPolicyViolations(self):
        url = 'https://api.64clouds.com/v1/getPolicyViolations?veid='+self.veid+'&api_key='+self.apikey
        try:
            getMsg = rq.get(url)
            getJson = json.loads(getMsg.text.replace("'",'"'))
            return getJson
        except:
            failed = json.loads('{"status":"error","name":"'+str(self.getPolicyViolations.__name__)+'"}')
            return failed

    def unsuspend(self,record_id):
        url = 'https://api.64clouds.com/v1/unsuspend?record_id='+record_id+'&veid='+self.veid+'&api_key='+self.apikey
        try:
            getMsg = rq.get(url)
            getJson = json.loads(getMsg.text.replace("'",'"'))
            return getJson
        except:
            failed = json.loads('{"status":"error","name":"'+str(self.unsuspend.__name__)+'"}')
            return failed
        
    def resolvePolicyViolation(self,record_id):
        url = 'https://api.64clouds.com/v1/resolvePolicyViolation?record_id='+record_id+'&veid='+self.veid+'&api_key='+self.apikey
        try:
            getMsg = rq.get(url)
            getJson = json.loads(getMsg.text.replace("'",'"'))
            return getJson
        except:
            failed = json.loads('{"status":"error","name":"'+str(self.resolvePolicyViolation.__name__)+'"}')
            return failed
        
    def getRateLimitStatus(self):
        url = 'https://api.64clouds.com/v1/getRateLimitStatus?veid='+self.veid+'&api_key='+self.apikey
        try:
            getMsg = rq.get(url)
            getJson = json.loads(getMsg.text.replace("'",'"'))
            return getJson
        except:
            failed = json.loads('{"status":"error","name":"'+str(self.getRateLimitStatus.__name__)+'"}')
            return failed
        
    def privateIpGetAvailableIps(self):
        url = 'https://api.64clouds.com/v1/privateIp/getAvailableIps?veid='+self.veid+'&api_key='+self.apikey
        try:
            getMsg = rq.get(url)
            getJson = json.loads(getMsg.text.replace("'",'"'))
            return getJson
        except:
            failed = json.loads('{"status":"error","name":"'+str(self.privateIpGetAvailableIps.__name__)+'"}')
            return failed
        
    def privateIpAsign(self,ip):
        url = 'https://api.64clouds.com/v1/privateIp/assign?ip='+str(ip)+'&veid='+self.veid+'&api_key='+self.apikey
        try:
            getMsg = rq.get(url)
            getJson = json.loads(getMsg.text.replace("'",'"'))
            return getJson
        except:
            failed = json.loads('{"status":"error","name":"'+str(self.privateIpAsign.__name__)+'"}')
            return failed
        
    def privateIpDelete(self,ip):
        url = 'https://api.64clouds.com/v1/privateIp/delete?ip='+str(ip)+'&veid='+self.veid+'&api_key='+self.apikey
        try:
            getMsg = rq.get(url)
            getJson = json.loads(getMsg.text.replace("'",'"'))
            return getJson
        except:
            failed = json.loads('{"status":"error","name":"'+str(self.privateIpDelete.__name__)+'"}')
            return failed