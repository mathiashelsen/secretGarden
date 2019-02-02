
-- t = require("ds18b20")
-- pin = 1 -- gpio0 = 3, gpio2 = 4

print("Running Application")

if adc.force_init_mode(adc.INIT_ADC)
then
  node.restart()
  return -- don't bother continuing, the restart is scheduled
end


-- MOISTURE MEASUREMENT --

port = 80


print("Creating Server")

srv=net.createServer(net.TCP)

print("Created Server")
srv:listen(port,
     function(conn)
        gconn = conn
        print("HTTP Request Received\n")
        local resp = "HTTP/1.1 200 OK\nContent-Type: text/html\nRefresh: 5\n\n"
        resp = resp .. string.format("%d\n", adc.read(0))
        gconn:send(resp)
        gconn:on("sent",function(conn) conn:close() end)
     end
)


-- TEMPERATURE MEASUREMENT --

-- mytimer = tmr.create()
-- mytimer:register(1000, tmr.ALARM_AUTO, readADC)
-- mytimer:start()

-- t = require('ds18b20')
-- 
-- port = 80
-- pin = 1 -- gpio0 = 3, gpio2 = 4
-- gconn = {} -- global variable for connection
-- 
-- print("Defining ReadOutTemp")
-- 
-- function readout(temp)
--   local resp = "HTTP/1.1 200 OK\nContent-Type: text/html\nRefresh: 5\n\n"
-- 
--   for addr, temp in pairs(temp) do
--     resp = resp .. string.format("Sensor\t%s\t%s\n", ('%02X:%02X:%02X:%02X:%02X:%02X:%02X:%02X '):format(addr:byte(1,8)), temp)
--   end
-- 
--   gconn:send(resp)
--   gconn:on("sent",function(conn) conn:close() end)
-- end
-- 
-- print("Creating Server")
-- 
-- srv=net.createServer(net.TCP)
-- 
-- print("Created Server")
-- srv:listen(port,
--      function(conn)
--         gconn = conn
--         print("HTTP Request Received\n")
--         -- t:read_temp(readout) -- default pin value is 3
--         t:read_temp(readout, pin)
--      end
-- )
