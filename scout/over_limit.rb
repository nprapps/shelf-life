require 'date'

class ShelfLifeNearingLimit < Scout::Plugin
  def build_report

    log_file_path = 'data/test.log'
    count = 0

    today = Date.today

    File.open(log_file_path) do |file|
      file.each do |line|

        file_date = line.split(' ')[0]
        file_time = line.split(' ')[1]

        this_date = Date.parse(file_date)

        if this_date == today
          if line.split(' ')[2] == 'INFO'
            count += 1
          end
        end

      end
    end

    report(:successful_posts => count)

  end
end
