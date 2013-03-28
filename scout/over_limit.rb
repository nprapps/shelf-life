require 'date'

class OverLimit < Scout::Plugin
  def build_report

    log_file_path = '/var/log/cook-your-cupboard.log'
    count = 0

    today = Date.today

    File.open(log_file_path) do |file|
      file.each do |line|

        file_date = line.split(' ')[0]
        file_time = line.split(' ')[1]

        this_date = Date.parse(file_date)

        if this_date == today
          if line.include?("photo upload limit")
            count += 1
          end
        end

      end
    end

    report(:over_limit_errors => count)

  end
end
